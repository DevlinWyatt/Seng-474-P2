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

	return dic1
	



dic1 = {}

dic1 = parseFile("data_10k_100.tsv")

