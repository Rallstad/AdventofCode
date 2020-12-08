from utils import readFile
import operator

ops = { "+": operator.add, "-": operator.sub } # legger til string operators som operators

lines = readFile('inputs/inputTask8.txt')

def accumulateAcc():
	acc = 0
	jmp = 1
	been = []
	index = 0
	repeated = False

	while not repeated:
		print(index)
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
				#print(j)	
				jmp = (-jmp)
				index = index + jmp	


		elif "acc" in lines[index]:
			#print(line)
			if "+" in lines[index]:
				num = int(lines[index].split("+",1)[1])
				#print(num)		
				acc = ops["+"](acc,num)
				#print(acc)
			elif "-" in lines[index]:
				num = int(lines[index].split("-",1)[1])
				#print(num)		
				acc = ops["-"](acc,num)
			index = index + 1
				#print(acc)
						#elif "-" in line:
				#print(ops["+"](1,1))
		elif "nop" in lines[index]:

			index = index + 1
	print(acc)
	return acc



def terminateCorrectly(lines):
	
	for line in lines:
		acc = 0
		jmp = 1
		been = []
		index = 0
		repeated = False

		if "jmp" in line:
			line = line.replace("jmp", "nop")
		elif "nop" in line:
			line = line.replace("nop", "jmp")

		while not repeated and -1 < index < len(lines):
			print(index)
			if index in been:
				repeated = 1
				break
			else:
				been.append(index)

			if "jmp" in lines[index]:
				if "+" in lines[index]:

					jmp = int(lines[index].split("+",1)[1])
					if index >= len(lines):
						print(acc)
						return acc
					else:
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

		if "jmp" in line:
			line = line.replace("jmp", "nop")
		elif "nop" in line:
			line = line.replace("nop", "jmp")


terminateCorrectly(lines)



