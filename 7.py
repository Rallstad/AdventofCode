from utils import readFile
import re

lines = readFile('inputs/inputTask7.txt')


def DigDeep(line, lines):
	splitLine = SplitLine(line)

	for bag in splitLine[1:]:
		if "o other" in splitLine[1]:
			continue

		if "shiny gold" in bag:
			return True

		child = SearchChild(bag, lines)
		shiny = DigDeep(child, lines)
		if shiny == True:
			return True


def SearchChild(bag, lines):
	bagColor = re.findall('[a-z]+', bag)
	bagColor = ' '.join(bagColor)
	for line in lines:
		if line.startswith(bagColor):
			return line
	print("something is wrong")
	return 0


def SplitLine(line):
	sl = line.replace('contain',',')
	sl = sl.split(',')
	sl[0] = sl[0].replace(' bags ', '')
	for elem in range(1,len(sl)):
		remove = ''.join(sl[elem].split(' ')[1-2])
		sl[elem] = sl[elem][2:]
		sl[elem] = sl[elem].replace(remove,'')
		sl[elem] = sl[elem].strip()
	return sl


def BagWithGoldBags(lines):
	shinyCount = 0
			
	for line in lines:
		shiny= DigDeep(line, lines)
		if shiny == True:
			shinyCount += 1
	return shinyCount

print(BagWithGoldBags(lines))