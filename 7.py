from utils import readFile
import re

lines = readFile('inputs/inputTask7.txt')

def findEmptyBags(line):
	emptyBags = []
	if "contain no other bags" in line:
		color = re.sub(' bags contain no other bags\.$', '', line)
		emptyBags.append(color)
	return emptyBags



def findTopLevelBags(line):
	topLevel = []
	color = ' '.join(line.split()[:2])
	topLevel.append(color)
	return topLevel


def splitLine(line):

 
	colorList = line.split(',')
	print(colorList)
	for elem in colorList:
		

	
	#print(colorList)

	

	return line

def calcNumShinyGoldBags(lines):
	top = []
	empty = []
	splitList = []
	 
	for line in lines:
		top.append(findTopLevelBags(line))
		empty.append(findEmptyBags(line))

	for line in lines:
		splitList.append(splitLine(line))

	
	#print(splitList)
		
#		for split in splitList:
#			if split in empty:
#				splitlist.remove(empty)


#	empty = findEmptyBags(lines)
	

#	for e in empty:
#		if e in top:
#			top.remove(e)

	
#	split = splitLines(top, lines)
#	print(split)
	num = 0


	#for line in lines:
		#if empty in line:

			#print(line)

	return num

#print(calcNumShinyGoldBags(lines))
calcNumShinyGoldBags(lines)


