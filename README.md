#K Means Clustering

''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''

@(#)Program:	    K-Means Clustering
@(#)Purpose:        To cluster given dataset into k clusters, visualize the clusters hence formed.
@(#)Author(s):      V.Rajagopal, Nikhil Pularru, Prakhar Jain

Run the program as follows:

python  Clustering.py  [input_txt_filename] \[value_of_k]  (On Windows)

OR

python3  Clustering.py  [input_txt_filename] \[value_of_k]  (On Linux)

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
