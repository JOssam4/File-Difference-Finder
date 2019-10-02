import sys


# Given file 1 and 2, return a string representing differences in the files
def findDifferencesAsString(file1, file2):
	file1Data = readImage(file1)
	file2Data = readImage(file2)
	file1Diff, file2Diff = compareFiles(file1Data, file2Data)
	file1DiffAsChars = map(chr, file1Diff)
	file2DiffAsChars = map(chr, file2Diff)
	file1DiffAsString = "".join(file1DiffAsChars)
	file2DiffAsString = "".join(file2DiffAsChars)
	print("differences in file1: {}".format(file1DiffAsString))
	print("differences in file2: {}".format(file2DiffAsString))


# Read the binary data found in the file. I call it readImage because usually this CTF challenge is done with two images.
def readImage(fileToRead):
	with open(fileToRead, "rb") as image1:
		img1Data = image1.read()
	return img1Data
  
# Given the binary data found in file1 and file2, return 2 lists, where each one contains the bytes that differ from each other.
def compareFiles(file1Data, file2Data):
	retFile1 = []
	retFile2 = []
	for f1Byte, f2Byte in zip(file1Data, file2Data):
		if (f1Byte != f2Byte):
			retFile1.append(f1Byte)
			retFile2.append(f2Byte)
	return (retFile1, retFile2)		


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("You have only specified one file.")
		sys.exit(1)
	else:
		file1 = sys.argv[1]
		file2 = sys.argv[2]
		diff = findDifferencesAsString(file1, file2)
    
