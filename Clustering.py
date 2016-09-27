''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''

#	@(#)Program:	    K-Means Clustering
#	@(#)Purpose:        To cluster given dataset into k clusters, visualize the clusters hence formed.
#	@(#)Author(s):      V.Rajagopal, Nikhil Pularru, Prakhar Jain

Run the program as follows:

python  Clustering.py  [input_txt_filename]  [value_of_k]  (On Windows)

OR

python3  Clustering.py  [input_txt_filename]  [value_of_k]  (On Linux)

INPUT FORMAT

	> The program assumes the input file contains one entry per row, where each entry consists of the x and y coordinate of a point in the 2D plane, separated by a single comma.

		eg. file.txt

		1,2
		2,3
		3,5
		4,6


External Dependencies:
	
	> numpy
	> pygame


OUTPUT

	> The program visualilzes the clustering, by updating the screen after every iteration of the clustering function. If the number of clusters is k, then k random visually distinct colours are generated, and one colour is assigned to each cluster.

''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''

import os
import sys
from pygame.locals import *
import random
import numpy as np
import colorsys
import pygame
import time
from math import sqrt
import subprocess


''' Global Variables ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 

k=0
space=[]
screencolors=[]
centroids=[]
screen=None
x_max=0
x_min=float("inf")
y_max=0
y_min=float("inf")

''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 




''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
def initialize():		# Initialization function for loading data into memory, initializing display canvas and selecting k random centroids.
	global space		# Space is the list of all points in the dataset, initialized to cluster "-1".
	global centroids
	global k
	global screen
	pygame.init()
	screen=pygame.display.set_mode((1366,768))		# Initializes Blank Canvas (1366*768 resolution)
	f=open(sys.argv[1], "r")						# File to read data from supplied as CL argument
	k=int(sys.argv[2])								# Number of clusters, k, supplied as CL argument
	initread=f.read().splitlines()
	f.close()
	for i in initread:
		space += [int(i.split(",")[0]), int(i.split(",")[1]), -1],

	for i in range(k):								# Selecting k random centroids
		n=random.randrange(len(space))
		centroids+=[[space[n][0],space[n][1], i+1],]
		space[n][2]=int(i+1)
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 




''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
def getdistance(a,b,c,d):							# Returns Euclidean distance between points (a,b) and (c,d)
	return sqrt(((d-b)**2) + ((c-a)**2))
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 




''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
def getcentroids():									# Computes new centroids after each clustering iteration
	global centroids
	global space
	newcentroids=[]
	for i in range(k):
		x=0
		y=0
		pts=0
		for point in space:
			if point[2]==(i+1):
				x+=point[0]
				y+=point[1]
				pts+=1
		newcentroids+=[[x/pts, y/pts, i+1],]
	if newcentroids==centroids:
		return 1
	else:
		centroids=newcentroids
		return 0
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 




''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
def cluster():										# The K-means Clustering function.
	global space 									# Computes distance of each point from all centroids and chooses the cluster with the min distance.
	global centroids
	for point in space:
		if point not in centroids:
			dist=getdistance(centroids[0][0], centroids[0][1], point[0], point[1])
			clust=1
			for centroid in centroids:
				ndist=getdistance(centroid[0], centroid[1], point[0], point[1])
				if ndist<dist:
					dist=ndist
					clust=centroid[2]
			point[2]=clust
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 




''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
def init_colors(k):									# Generates K random visually-distinct colours.
	global screencolors
	colors=[]
	for i in np.arange(0., 360., 360. / k):
		hue = i/360.
		lightness = (50 + np.random.rand() * 10)/100
		saturation = (90 + np.random.rand() * 10)/100
		colors+=[i for i in colorsys.hls_to_rgb(hue, lightness, saturation)],
	for i in colors:
		screencolors+=[[int(j*255) for j in i],]
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 


''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
def get_range():					# Maximum and minimum values of ordinates and abcissa initialized globally.
	global x_max
	global x_min
	global y_max
	global y_min
	global space
	for point in space:
		if point[0]>x_max:
			x_max=point[0]
		elif point[0]<x_min:
			x_min=point[0]
		if point[1]>y_max:
			y_max=point[1]
		elif point[1]<y_min:
			y_min=point[1]
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 



''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
def main():
	initialize()
	init_colors(k)
	change=0
	converged=0
	get_range()
	start=time.strftime("%H:%M:%S", time.gmtime())
	stop="Null"
	OS="Def"
	if "Linux" in os.uname():
		OS="Linux"
	else:
		OS="Windows"
	if OS=="Linux":
		RAM=int(float(subprocess.check_output(["cat /proc/meminfo | grep MemTotal | awk '{print $2}'"], shell=True).decode('ascii').strip())/1024)+1
	while True:										# Loop continuously checks for an exit event, i.e. a click on the close button
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		for point in space:							# Plots each point on the canvas, in the colour of its current cluster
			pygame.draw.circle(screen, screencolors[point[2]-1], (int((float(point[0]/(x_max))*1366)-int(((x_min/x_max)*1366)/2)), int((float(point[1]/(y_max))*768)-int(((y_min/y_max)*768)/2))), 1, 0)
		if OS=="Linux":
			perc=float(subprocess.check_output(["ps aux | grep python3\ Clustering"], shell=True).decode('ascii').strip().split()[3])
		pygame.display.update()
		cluster()
		change=getcentroids()
		if change==0 and OS=="Linux":
			os.system("clear")
			print("Memory used : " + str(perc*RAM/100) + " Mb")
		elif change==1 and OS=="Linux":
			if converged==0:
				if (isinstance(start, str)):
					start=[int(i) for i in start.split(":")]
				if (isinstance(stop, str)):
					stop=time.strftime("%H:%M:%S", time.gmtime())
					stop=[int(i) for i in stop.split(":")]
				time_elapsed=[stop[i]-start[i] for i in range(3)]
				os.system("clear")
				print("Memory used : " + str(perc*RAM/100) + " Mb")
				print("Time to Converge : " + str(time_elapsed[0]) + " Hrs, " + str(time_elapsed[1]) + " Mins, " + str(time_elapsed[2]) + " Sec.")
				print("Press Ctrl + C to exit.")
				converged=1
		else:
			if converged==0 and change==1:
				start=[int(i) for i in start.split(":")]
				stop=time.strftime("%H:%M:%S", time.gmtime())
				stop=[int(i) for i in stop.split(":")]
				time_elapsed=[stop[i]-start[i] for i in range(3)]
				print("Time to Converge : " + str(time_elapsed[0]) + " Hrs, " + str(time_elapsed[1]) + " Mins, " + str(time_elapsed[2]) + " Sec.")
				print("Memory Stats Unavailable on this OS. Press Ctrl + C to exit.")
				converged=1
		pygame.display.update()
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 




if __name__ == "__main__":
	main()
	