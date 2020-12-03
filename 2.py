from utils import readFile
passwords = readFile('inputs/inputTask2.txt')

def Task2a(passwords):
    count = 0
    for p in passwords:
        limitLow = p.split("-")[0]
        limitHigh = p.split('-')[1].split(' ')[0]
        reqChar = p.split(' ')[1].split(':')[0]
        passString = p.split(' ')[2]
        passStringCharCount = passString.count(reqChar)
        if passStringCharCount >= int(limitLow) and passStringCharCount <= int(limitHigh):
            count = count + 1
    return count


def Task2b(passwords):
    count = 0
    for p in passwords:
        first = int(p.split("-")[0])-1
        second = int(p.split('-')[1].split(' ')[0])-1
        reqChar = p.split(' ')[1].split(':')[0]
        passString = p.split(' ')[2]
        if (passString[first] == reqChar and passString[second] != reqChar) or (passString[first] != reqChar and passString[second] == reqChar):
            count = count + 1
    return count        


print(Task2a(passwords))
print(Task2b(passwords))