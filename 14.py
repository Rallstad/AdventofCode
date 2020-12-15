from utils import readFile
import re

lines = readFile('inputs/inputTask14.txt')

def GetMemAddress(l):
    print((l[0].split('['))[1].split(']')[0])
    return int((l[0].split('['))[1].split(']')[0])


def GetMemBinaryValue(l, bit):
    binaryValueList = []
    value = int(l[1].strip())
    binaryValue = "{0:b}".format(value)
    for elem in binaryValue:
        binaryValueList.append(elem)

    while len(binaryValueList) != bit:
        binaryValueList.insert(0,'0')
    print("binaryValueList")
    print(binaryValueList)
    return binaryValueList

#def ConvertBinary2Int(binaryList):

def GetMaskList(l, maskList):
    binaryMask = l[1]
    maskList = []
    print("binaryMask")
    print(binaryMask)
    for b in binaryMask:

        maskList.append(b)
    print("maskList")
    print(maskList)
    return maskList

def MaskValue(maskList, memoryBinaryList):
    count = 0

    for mask in maskList:

        if 'X' not in mask:
            memoryBinaryList[count] = mask
        count += 1
        
    maskedMemoryBinaryList = memoryBinaryList
    return maskedMemoryBinaryList


def MaskValueWithFloating(maskList, memoryBinaryList):
    count = 0
    binaryListList = []
    print("masklist")
    print(maskList)

    for mask in maskList:

        if 'X' not in mask:
            memoryBinaryList[count] = mask
        

        elif 'X' in mask:
            memoryBinaryList[count] = 0

            binaryListList.append(memoryBinaryList)
            memoryBinaryList[count] = 1
            binaryListList.append(memoryBinaryList)
        count += 1
    return binaryListList



def CalcSumOfMemValues(lines):
    maskList = []
    total = 0
    bit = 36
    memAddressDict = {}
    memAddressDictUsingFloatingBit = {}
    for line in lines:
        
        l = line.split(' = ')

        if l[0] == 'mask':
            maskList = GetMaskList(l, maskList)
        else:
            memoryAddress = GetMemAddress(l)
            
            memoryBinaryList = GetMemBinaryValue(l, bit)
            maskedMemoryBinaryList = MaskValue(maskList, memoryBinaryList)
            maskedMemoryBinaryListListWithFloating = MaskValueWithFloating(maskList, memoryBinaryList)
            value = int("".join(str(i) for i in maskedMemoryBinaryList),2) #convert binary list maskedMemoryBinaryList to integer
            memAddressDict[memoryAddress] = value

    print(maskedMemoryBinaryListListWithFloating)
    return
    
    for v in memAddressDict:
        print("dictionary")
        print(memAddressDict[v])
        total += memAddressDict[v]
    return total



print(CalcSumOfMemValues(lines))


