inputFile = open('input.txt', 'r')
data = inputFile.readlines()


def task1a():
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			value = int(data[i]) + int(data[j])
			if value == 2020:
				print("%d + %d = %d" %(int(data[i]), int(data[j]), value))
				print("product: %d" %(int(data[i]) * int(data[j])))

def task1b():
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			for k in range(j+1, len(data)):
				value = int(data[i]) + int(data[j]) + int(data[k])
				if value == 2020:
					print("%d + %d + %d = %d" %(int(data[i]), int(data[j]), int(data[k]), value))
					print("product: %d" %(int(data[i]) * int(data[j]) * int(data[k])))

print("task 1a")
task1a()
	
print("task 1b")
task1b()



