#!/usr/bin/env python3
import numpy as np
import sys


#######################
####  LORIN SOURA #####
####      &       #####
#### DEVLIN WYATT #####
#######################


####################
#### Functions #####
####################

#Method used to Parse the file into a dictionary
def parseFile(filename):
   print("Parsing file...")

   f = open(filename)

   N = int(f.readline().rstrip())
   D = int(f.readline().rstrip())

   #skip the header row
   f.readline()

   dic1 = {}

   for i in range(N):
      x = f.readline().rstrip().split('\t')
      dic1[i] = {"label": float(x[0]), "fs": []}

      for j in range(D):
         dic1[i]["fs"].append(float(x[j+1]))
         
   print("...File parsed.\n")
   return D, N, dic1


#Used to write the output, still requires coefficient data.
def writeOutput(D, W, filename):
   print("Writing results to {}.csv...".format(filename))

   header = []
   coefficients = []

   for i in range(1, D):
      header.append("w" + str(i))
      coefficients.append(str(W[i-1])) #This needs actual data to append!
   header.append("w0")
   

   h = "\t".join(header) + "\n"
   c = "\t".join(coefficients)

   #Has to be in tsv format
   f = open("{}.tsv".format(filename), "w")
   f.write(h+c)

   print("...{}.tsv saved.\n".format(filename))


'''
Question 1 is an algorithm that uses the normal equation to learn linear regression models.
The normal Equation is W = (X^T * X)^-1 * X^T * Y
And the linear regression hypothesis is h(x) = w^T * X
'''
def question1(N, D):
   print("Starting Question 1...")
   W = []
   #Need to create lists of data by collumns
   #this should count as transpose (turning a collumn into a row)
   #y wont change so we'll compute it first.
   y = []
   for i in range(N):
      y.append(data[i]["label"])

   #this is where the main algorithm will start for Question 1
   for j in range(D):
      x = [] 

      for i in range(N):
         x.append(data[i]["fs"][j]) 

      #Need to calculate X^T * X, should give us one value.
      #should just be x_1^2 + x_2^2 + ... + x_n^2
      p=0
      for i in x:
         p = p + i*i
      p = 1/p

      #need to calculate X^T * Y which is X_1*Y_1 + X_2*Y_2 + ... + X_n*Y_n
      l=0
      for i in range(N):
         l = l + x[i]*y[i] 

      w = p*l

      #write all values of w to a list
      W.append(w)

   print("...Finished Question 1.\n")

   writeOutput(D+1, W, "Q1")

   return 


def question2():
   return None


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
   for counter, item in enumerate(dictionaries):
      #feature_list = np.array(dictionaries[counter]['fs'])
      #feature_ones = np.ones((feature_list.shape[0]))
      #feature_matrix = np.c_[feature_list,feature_ones]
      # Generate a matrix where each data point is a 2D feature vector
      fcounter = 0
      feature_matrix = []
      for count, feature in enumerate(dictionaries[counter]['fs'],0):
         #sys.stdout.write(str(count) + ' ')
         # insert a column of 1's as the first entry in the feature vector
         feature_matrix.append([feature,1])  
     
      weight_matrix=np.random.uniform(size=(len(feature_matrix)-1))
      print(weight_matrix)
      # loss_function = 1/(2*N)*(y-wt*x)
 
   # initialize weight matrix to have the same number of columns as 
   # Loop until we reach T epochs OR loss is sufficently low OR
      # Wgradient = evaluate_gradient(loss, data, W) using:
         # loss function
         # data
         # weight matrix
      # W += -1 * learning_rate * Wgradient 


###############
#### MAIN #####
###############
#############
###########
#########
#######
#####
####
###
##
#

data = {}
filename = "data_100k_300.tsv"

D, N, data = parseFile(filename)

question1(N, D)

question2()

#question3_a(data,filename)


exit(0)
#git clone https://github.com/DevlinWyatt/Seng-474-P2

