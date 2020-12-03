from utils import readFile

lineArr = readFile('inputs/inputTask3.txt')

def task3a(lineArr):
    treeCount = 0
    elem = 0

    for line in lineArr:
        if line[elem] == "#":
            treeCount = treeCount + 1
        elem = (elem + 3) % 31
    
    return treeCount


def task3b(lineArr):
    vStepSize = [1, 1, 1, 1, 2]
    hStepSize = [1, 3, 5, 7, 1]
    treeCountProduct = 1

    for step in range(len(vStepSize)):
        treeCount = 0
        elem = 0
        for line in lineArr[::vStepSize[step]]:
            if line[elem] == "#":
                treeCount = treeCount + 1
            elem = (elem + hStepSize[step]) % 31
        treeCountProduct = treeCountProduct * treeCount

    return treeCountProduct


print(task3a(lineArr))
print(task3b(lineArr))
