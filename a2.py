#!/usr/bin/env python3
import numpy as np
import sys

#Method used to Parse the file into a dictionary of dictionaries
def parseFile(filename):
	print("Parsing file")

	f = open(filename)
   # Number of data points
	N = int(f.readline().rstrip())
   # Number of features
	D = int(f.readline().rstrip())

	#skip the header row
	f.readline()

	dic1 = {}
	for i in range(N):
		x = f.readline().rstrip().split('\t')
		dic1[i] = {0: x[0], 1: {}}

		for j in range(D):
			dic1[i][1].setdefault(j,[1,float(x[j+1])])
	print("File parsed.")
	return dic1

def cost_function(feature_count, x, y):
   return 0

def question3_a(dictionaries,filename):
   # epoch_limit
   T = 20 
   learning_rate = 0.000001
   batch_size = 1
   bias = 1
   f = open(filename)
   # Get number of data points
   N = int(f.readline().rstrip())
   # Get number of features
   D = int(f.readline().rstrip())
   f.close() #-------------------------------------
   for counter, item in enumerate(dictionaries):
      # Generate a matrix where each data point is a 2D feature vector
      Y = dictionaries[counter][0]

      print(dictionaries[counter][1]) # feature_matrix with ones in first column 
      # The feature set is a dictionary of int labels 0 to 99
      # feature set dictionary contains a list [1, x-value]
      # Access using dictionaries[counter][1]
        
  
      # Get random weight for calculation  
      # loss_function = 1/(2*N)*(y-wt*x) where N is the number of features.
 
      # initialize weight matrix to have the same number of columns as 
      # Loop until we reach T epochs OR loss is sufficently low OR
         # Wgradient = evaluate_gradient(loss, data, W) using:
            # loss function
            # data
            # weight matrix
      

filename = "data_10k_100.tsv"
dic1 = parseFile(filename)
question3_a(dic1,filename)
#print(dic1[1])
exit(0)
# git clonegit clone https://github.com/DevlinWyatt/Seng-474-P2
# git init
# git config user.name "someone"
# git config user.email "someone@someplace.com"
# git add *
# git commit -m "some init msg"

