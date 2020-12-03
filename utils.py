def readFile(input_file):
	with open(input_file) as f:
		lines = f.read().splitlines()
		numArr = [line for line in lines]
	return numArr