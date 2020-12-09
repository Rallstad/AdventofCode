from utils import readFile
import math

lines = readFile('inputs/inputTask9.txt')




def populatePreamble(lines):
	preamble = []
	count = 0
	for line in lines:
		if count == 25:
			break
		preamble.append(lines[count])
		count = count + 1

	return preamble


def moveList(count, lines, preamble):
	preamble.remove(preamble[0])
	preamble.append(lines[count])

	return preamble

def isNumberSumOfPrevious(lines, preamble, nextLine):
	for i in range(0,len(preamble)):
		for j in range(0,len(preamble)):
			value = int(preamble[i]) + int(preamble[j])

			if value == int(nextLine):

				return True

	return False


def findNumber(lines):
	preamble = populatePreamble(lines)
	count = len(preamble)


	for line in lines:
		
		nextLine = int(lines[count])
		if not isNumberSumOfPrevious(lines, preamble, nextLine):
			return nextLine

		if len(preamble) == 25:
			preamble = moveList(count, lines, preamble)
			#print(len(preamble))
		else:
			return nextLine
		count = count + 1


	print("Ingen feil")
	return 0



print(findNumber(lines))



def findContiguous(lines):
	preamble = populatePreamble(lines)
	count = len(preamble)
	num = int(findNumber(lines))
	targetValue = 0
	preambleIndex = 0

	for i in range(0,len(lines)):
		for line in preamble:
			
			targetValue = targetValue + int(line)

			if targetValue == num:
				maxVal = max(preamble[:preambleIndex])
				minVal = min(preamble[:preambleIndex])

				return int(maxVal) + int(minVal)

			preambleIndex = preambleIndex + 1

		targetValue = 0	
		preambleIndex = 0	
		preamble = moveList(count, lines, preamble)
		count = count + 1

	print("Ingen feil")
	return 0


print(findContiguous(lines))