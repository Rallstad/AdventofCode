from utils import readFile
import operator

ops = { "+": operator.add, "-": operator.sub } # legger til string operators som operators

lines = readFile('inputs/inputTask8.txt')

def accumulateAcc(lines):
	acc = 0
	jmp = 1
	been = []
	index = 0
	repeated = False

	while not repeated:
		if index in been:
			repeated = 1
			break
		else:
			been.append(index)

		if "jmp" in lines[index]:
			if "+" in lines[index]:
				jmp = int(lines[index].split("+",1)[1])
				index = index + jmp

			elif "-" in lines[index]:
				jmp = int(lines[index].split("-",1)[1])
				index = index - jmp	

		elif "acc" in lines[index]:
			if "+" in lines[index]:
				num = int(lines[index].split("+",1)[1])
				acc = ops["+"](acc,num)
			elif "-" in lines[index]:
				num = int(lines[index].split("-",1)[1])
				acc = ops["-"](acc,num)
			index = index + 1

		elif "nop" in lines[index]:
			index = index + 1

	return acc



def terminateCorrectly(lines):
	count = -1
	for line in lines:
		if count != len(lines):
			count = count + 1
		else:
			print("no valid results..")
			return 0

		acc = 0
		jmp = 0
		been = []
		index = 0
		repeated = False
		
		#change jmp and nop line for line in lines 
		if "jmp" in lines[count]:
			lines[count] = lines[count].replace("jmp", "nop")
		elif "nop" in lines[count]:
			lines[count] = lines[count].replace("nop", "jmp")

		while not repeated:
			if index in been:
				repeated = 1
				break
			else:
				been.append(index)

			if "jmp" in lines[index]:
				if "+" in lines[index]:
					jmp = int(lines[index].split("+",1)[1])
					index = index + jmp

				elif "-" in lines[index]:
					jmp = int(lines[index].split("-",1)[1])
					jmp = (-jmp)
					index = index + jmp

			elif "acc" in lines[index]:
				if "+" in lines[index]:
					num = int(lines[index].split("+",1)[1])
					acc = ops["+"](acc,num)

				elif "-" in lines[index]:
					num = int(lines[index].split("-",1)[1])
					acc = ops["-"](acc,num)

				index = index + 1

			elif "nop" in lines[index]:
				index = index + 1

			if index == len(lines) -1:
				print("done")
				return acc
		
		#change back the jmp and nop lines
		if "jmp" in lines[count]:
			lines[count] = lines[count].replace("jmp", "nop")
		elif "nop" in lines[count]:
			lines[count] = lines[count].replace("nop", "jmp")

#print(terminateCorrectly(lines))
print(accumulateAcc(lines))


