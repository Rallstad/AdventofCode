from utils import readFile
import math
lines = readFile('inputs/inputTask10.txt')
lines = [int(line) for line in lines]
print(lines)



#for line in lines:
#print(line)
def FindChain(lines):
    singleHop = 1
    doubleHop = 2
    tripleHop = 3

    numSingleHop = 0
    numDoubleHop = 0
    numTripleHop = 0

    deviceJolts = 3
    minJolt = min(lines)
    maxJolt = max(lines)
    current = minJolt

    if current == 1:
        numSingleHop = numSingleHop + 1
    elif current == 2:
        numDoubleHop = numDoubleHop + 1
    elif current == 3:
        numTripleHop = numTripleHop + 1

    for line in lines:
        if current == maxJolt:
            numTripleHop = numTripleHop + 1
            total = numSingleHop * numTripleHop
            return total

        if (current + singleHop) in lines:
            current = current + singleHop
            numSingleHop = numSingleHop + 1

        elif (current + doubleHop) in lines:
            current = current + doubleHop
            numDoubleHop = numDoubleHop + 1

        elif (current + tripleHop) in lines:
            current = current + tripleHop
            numTripleHop = numTripleHop + 1
        else:            
            return False
    

print(FindChain(lines))

