from utils import readFile

intNumArr = [int(line) for line in readFile('inputs/inputTask1.txt')]

def task1a(intNumArr):
	for i in range(len(intNumArr)):
		for j in range(i+1, len(intNumArr)):
			value = intNumArr[i] + intNumArr[j]
			if value == 2020:
				print("%d + %d = %d" %(intNumArr[i], intNumArr[j], value))
				print("product: %d" %(intNumArr[i] * intNumArr[j]))

def task1b(intNumArr):
	for i in range(len(intNumArr)):
		for j in range(i+1, len(intNumArr)):
			for k in range(j+1, len(intNumArr)):
				value = intNumArr[i] + intNumArr[j] + intNumArr[k]
				if value == 2020:
					print("%d + %d + %d = %d" %(intNumArr[i], intNumArr[j], intNumArr[k], value))
					print("product: %d" %(intNumArr[i] * intNumArr[j] * intNumArr[k]))

print("task 1a")
task1a(intNumArr)

print("task 1b")
task1b(intNumArr)



