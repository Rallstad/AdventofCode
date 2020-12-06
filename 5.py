from utils import readFile
import bisect

lines = readFile('inputs/inputTask5.txt')

def getSeatBinary(line):
    seatsInBinary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = 0
    for letter in line:
        if letter == 'B' and index <= 6:
            seatsInBinary[index] = 1
                
        elif letter == 'R':
            seatsInBinary[index] = 1
        index = index + 1
    return seatsInBinary


def getSeatID(seatsInBinary):
    row = 0
    col = 0
    indexRow = 6
    indexCol = 2
    for elem in seatsInBinary:
        if indexRow >= 0:
            row = row + elem * 2**indexRow
            indexRow = indexRow - 1
        else:
            col = col + elem * 2**indexCol
            indexCol = indexCol - 1
    seatID = row * 8 + col

    return int(seatID)

def getBinaryValue(index, seatsInBinary):
    value = 0
    for elem in seatsInBinary:
        if index >= 0:
            value = value + elem * 2**index
            index = index - 1
    return value


def getHighestID(lines):
    highest = 0
    for line in lines:
        binary = getSeatBinary(line)
        seatID = getSeatID(binary)
        if seatID >= highest:
            highest = seatID

    return highest

def getLowestID(lines):
    lowest = getHighestID(lines)
    for line in lines:
        binary = getSeatBinary(line)
        seatID = getSeatID(binary)
        if seatID <= lowest:
            lowest = seatID

    return lowest

def getYourSeatID(lines):
    IDs = []
    missingIDs = []
    lowest = getLowestID(lines)
    highest = getHighestID(lines)
    count = lowest
    print(lowest)
    print(highest)
    for line in lines:
        binary = getSeatBinary(line)
        index = len(binary) - 1
        ID = getSeatID(binary)
        if ID not in IDs:
            bisect.insort(IDs, ID)
    for elem in IDs:
        if count in IDs:
            count = count + 1
            continue
        else:
            missingIDs.append(count)
            count = count + 1
    return missingIDs

            


print(getYourSeatID(lines))

print(getHighestID(lines))