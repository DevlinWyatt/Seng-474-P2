#!/python3


#######################
####  LORIN SOURA #####
####      &		  #####
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

D, N, data = parseFile("data_10k_100.tsv")
writeOutput(D+1)


