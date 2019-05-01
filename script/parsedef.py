outFile = open("tensorflow.def", "w")
outFile.write("EXPORTS")
outFile.write("\n")

with open("tensorflowTmp.def") as f:
	for line in f:
		lineList = line.split()
		outFile.write(lineList[-1])
		outFile.write("\n")

outFile.close()