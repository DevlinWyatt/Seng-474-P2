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
   print("Parsing file")

   f = open(filename)

   N = int(f.readline().rstrip())
   D = int(f.readline().rstrip())

   #skip the header row
   f.readline()

   dic1 = {}

   for i in range(N):
      x = f.readline().rstrip().split('\t')
      dic1[i] = {"label": x[0], "fs": []}

      for j in range(D):
         dic1[i]["fs"].append(float(x[j+1]))
         
   print("File parsed.")
   return D, N, dic1


#Used to write the output, still requires coefficient data.
def writeOutput(D):
   print("Writing results to output.csv")

   header = []
   coefficients = [""]

   for i in range(1, D):
      header.append("w" + str(i))
      coefficients.append("") #This needs actual data to append!
   header.append("w0")
   

   h = "\t".join(header) + "\n"
   c = "\t".join(coefficients)

   #Has to be in tsv format
   f = open("output.tsv", "w")
   f.write(h+c)

   print("output.tsv saved.")


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
filename = "data_10k_100.tsv"

D, N, data = parseFile(filename)


#Need to create lists of data by collumns
#this should count as transpose (turning a collumn into a row)
#y wont change so we'll compute it first.
y = []
for i in range(N):
   y.append(data[i]["label"])

#this is where the main algorithm will start for Question 1
x = [] 
for i in range(N):
   x.append(data[i]["fs"][0]) #This 0 will be 'j' in a loop once the algorithm is complete.


writeOutput(D+1)

question3_a(dic1,filename)

exit(0)
#git clonegit clone https://github.com/DevlinWyatt/Seng-474-P2

