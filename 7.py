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
	print(sl)
	return sl


def BagWithGoldBags(lines):
	shinyCount = 0
			
	for line in lines:
		shiny= DigDeep(line, lines)
		if shiny == True:
			shinyCount += 1
	return shinyCount

#print(BagWithGoldBags(lines))




# part b

def SplitIntoBagsAndNumbers(line):
	sl = line.replace('contain',',')
	sl = sl.split(',')
	sl[0] = sl[0].replace(' bags ', '')
	for elem in range(1,len(sl)):
		sl[elem] = sl[elem].strip()
	print("sl")
	print(sl)
	return sl

def GetNumberOfBagType(elem):
	num = ''.join(re.findall('[0-9]+', elem))
	if num.isdigit():
		return int(num)


def FindFactors(line, lines, factorList):
	
	if "no other bags." in splitLine:
		factorList.append("EOL")
		return factorList


		factorList.append(GetNumberOfBagType(bag)) # multiply number of bags in element with product

		child = SearchChild(bag, lines)
		print("child")
		print(child)
		FindFactors(child, lines, factorList)
	return factorList
	

def FindTotalBagCount(lines):
	bag = "shiny gold"
	line = SearchChild(bag, lines) # find the shiny gold line
	factorList = []
	totalBagsInShinyGoldBag = 1
	splitLine = SplitIntoBagsAndNumbers(line)

	for bag in splitLine[1:]:
		factorList.append(GetNumberOfBagType(bag)) # multiply number of bags in element with product

		factorList = FindFactors(splitLine, lines, factorList)
		print(factorList)
		numOfBagsInStrain = 1

	for factor in factorList:
		if factor != 'EOL':
			numOfBagsInStrain *= factor
		else:
			totalBagsInShinyGoldBag += numOfBagsInStrain
			print(numOfBagsInStrain)
			numOfBagsInStrain = 1

	totalBagsInShinyGoldBag *= 2
	totalBagsInShinyGoldBag -= 2 #remove 2 because of formula: 2 * 2**x - 1, and the shiny gold bag
	return totalBagsInShinyGoldBag

print(FindTotalBagCount(lines))



