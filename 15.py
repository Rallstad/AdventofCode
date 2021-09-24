from utils import readFile
import re

line = readFile('inputs/inputTask15.txt')

def GetLastTwoInstances(refNumber, prevNumbers):
    lastTwoSpoken = []
    count = 0
    for num in prevNumbers:
        if num == refNumber:
            lastTwoSpoken.append(count)
            if len(lastTwoSpoken) > 2:
                lastTwoSpoken.pop(0)
        count += 1

    return lastTwoSpoken

def GetNthNumber(line, iteration):
    prevNumbers = []
    startNumbers = line[0].split(',')
    startNumbers = [int(startNumber) for startNumber in startNumbers]
    currNum = -1
    nextNum = -1
    lastSpokenDict = {}
    beforeLastSpokenDict = {}
    count = 1
    for num in startNumbers:
        prevNumbers.append(num)
        if num not in lastSpokenDict:
            lastSpokenDict.update({num: count})
            beforeLastSpokenDict.update({num: count})
        count += 1
    currNum = startNumbers[len(startNumbers)-1]
    print(lastSpokenDict)
    print(prevNumbers)

    for num in range(len(startNumbers), iteration):
        lastSpokenDict.update({currNum: count})
        lastTwo = GetLastTwoInstances(currNum, prevNumbers)
        if currNum in prevNumbers[:len(prevNumbers)-1]:
            lastSpokenIndex = lastSpokenDict[currNum]
            currNum = abs(lastTwo[0] - lastTwo[1])
            prevNumbers.append(currNum)

        elif currNum not in prevNumbers[:len(prevNumbers) - 1]:
            currNum = 0
            prevNumbers.append(currNum)

        lastSpokenDict.update({currNum: count})
        count += 1
    
    return(currNum)
    
def main():
    iteration = 2020
    taskA = GetNthNumber(line, iteration)
    iteration = 30000000
    taskB = GetNthNumber(line, iteration)
    return taskA, taskB

print(main())


    
