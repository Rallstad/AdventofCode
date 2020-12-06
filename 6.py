from utils import readFile
import bisect

lines = readFile('inputs/inputTask6.txt')



def listDistinctGroupChars(group):
    joined = ''.join(group)
    distinct = list(set(joined))
    return distinct

def findCommonGroupAnswers(group):
    listList = []
    for elem in group:
        distinct = list(set(elem))
        listList.append(distinct)

    result = set(listList[0])
    for s in listList[1:]:
        result.intersection_update(s)
    return len(result)


def calcGroupValue(group):
    count = 0
    l = listDistinctGroupChars(group)
    for elem in l:
        count = count + 1
    return count

def getLastLine():
    secondLastLine = None
    astLine = None
    with open('inputs/inputTask6.txt') as infile:
        secondLastLine, lastLine = infile.readline(), infile.readline()
        for line in infile:
            
            secondLastLine = lastLine
            #print("secondLastLine: " + secondLastLine)
            lastLine = line
            #print("lastLine: " + lastLine)
    return lastLine, secondLastLine

def getTotalDistinct(lines):
    group = []
    totalDistinct = 0

    for line in lines:
        if line:
            print(line)
            group.append(line)
            #print(group)
        else:
            #print(group)
            groupValue = calcGroupValue(group)
            totalDistinct = totalDistinct + groupValue
            group = []
    return totalDistinct

def getTotalCommon(lines):
    group = []
    totalCommon = 0

    for line in lines:
        if line:
            group.append(line)
        else:
            common = findCommonGroupAnswers(group)
            totalCommon = totalCommon + common
            group = []
    return totalCommon


    

print(getTotalDistinct(lines))
print(getTotalCommon(lines))
