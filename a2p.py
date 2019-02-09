#!/python3

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
	
def writeOutput(D):
	print("Writing results to output.csv")

	header = []
	coefficients = [""]

	for i in range(1, D):
		header.append("w" + str(i))
		coefficients.append("")
	header.append("w0")
	

	h = "\t".join(header) + "\n"
	c = "\t".join(coefficients)

	#Has to be in tab format
	# string \t string \t string \n
	# string \t string \t string \n
	f = open("output.csv", "w")
	f.write(h+c)
	#for i in range(D):
		#f.write(header[i] + )
	print("output.csv saved.")


data = {}

D, N, data = parseFile("data_10k_100.tsv")

writeOutput(D)


