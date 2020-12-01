def readFile():
	inputFile = open('input.txt', 'r')
	data = inputFile.readlines()
	num = [int(line) for line in data]
	return num
	
def task1a():
	num = readFile()
	for i in range(len(num)):
		for j in range(i+1, len(num)):
			value = num[i] + num[j]
			if value == 2020:
				print("%d + %d = %d" %(num[i], num[j], value))
				print("product: %d" %(num[i] * num[j]))

def task1b():
	num = readFile()
	for i in range(len(num)):
		for j in range(i+1, len(num)):
			for k in range(j+1, len(num)):
				value = num[i] + num[j] + num[k]
				if value == 2020:
					print("%d + %d + %d = %d" %(num[i], num[j], num[k], value))
					print("product: %d" %(num[i] * num[j] * num[k]))

print("task 1a")
task1a()

print("task 1b")
task1b()



