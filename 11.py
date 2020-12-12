from utils import readFile
import copy

lines = readFile('inputs/inputTask11.txt')

def convert2Array(lines):
    lineCount = 0
    for line in lines:
        for spot in line:
            splitted = [spot for spot in line]
            lines[lineCount] = splitted
        lineCount += 1
    return lines


def PadLines(lines):
    # pad the top and bottom of grid of lines to avoid some corner cases
    pad = '0'*len(lines[0])
    lines.insert(0,pad)
    lines.insert(len(lines)+1,pad)
    lineCount = 0
    for line in lines:
        line = '0' + line + '0'
        lines[lineCount] = line
        lineCount += 1

    return lines


def CheckAdjacentSeats(splittedLines, lineCount, spotCount, acceptedOccupied):
    adjacentCount = 0
    if splittedLines[lineCount][spotCount - 1] == '#':
        adjacentCount += 1
    if splittedLines[lineCount][spotCount + 1] == '#':
        adjacentCount += 1
    if splittedLines[lineCount - 1][spotCount - 1] == '#':
        adjacentCount += 1
    if splittedLines[lineCount - 1][spotCount + 1] == '#':
        adjacentCount += 1
    if splittedLines[lineCount + 1][spotCount - 1] == '#':
        adjacentCount += 1
    if splittedLines[lineCount + 1][spotCount + 1] == '#':
        adjacentCount += 1
    if splittedLines[lineCount - 1][spotCount] == '#':
        adjacentCount += 1
    if splittedLines[lineCount + 1][spotCount] == '#':
        adjacentCount += 1
    if adjacentCount > acceptedOccupied:
        return False
    else:
        return True
    
    
def ChangeSeating(splittedLines):
    changedSeating = 0  
    lineCount = 0
    spotCount = 0
    newLines = copy.deepcopy(splittedLines)

    for line in splittedLines:
        for spot in line:
            if spot == 'L':
                acceptedOccupied = 0
                if CheckAdjacentSeats(newLines, lineCount, spotCount, acceptedOccupied):
                    splittedLines[lineCount][spotCount] = '#'
                    changedSeating += 1

            elif spot == '#':
                acceptedOccupied = 3
                if not CheckAdjacentSeats(newLines, lineCount, spotCount, acceptedOccupied):
                    splittedLines[lineCount][spotCount] = 'L'
                    changedSeating += 1
            spotCount += 1
        spotCount = 0
        lineCount += 1
    return changedSeating, splittedLines


def CountOccupied(lines):
    occupied = 0
    for line in lines:
        for spot in line:
            if spot == '#':
                occupied += 1

    return occupied


def mainA(lines):
    paddedLines = PadLines(lines)
    splittedLines = convert2Array(paddedLines)
    count = 0
    while True:
        changedSeating, changedLines = ChangeSeating(splittedLines)
        newLines = changedLines[:]
        if changedSeating == 0:
            occupied = CountOccupied(changedLines)
            print(occupied)

            return occupied

        
mainA(lines)


#part two

def CheckSeatsInSight(splittedLines, lineCount, spotCount, acceptedOccupied):
    adjacentCount = 0
    endReached = 0
    step1 = 1
    step2 = 1
    step3 = 1
    step4 = 1
    step5 = 1
    step6 = 1
    step7 = 1
    step8 = 1

    while endReached <= 7:
        if step1 > 0:
            if splittedLines[lineCount][spotCount - step1] == '#':
                adjacentCount += 1
                endReached += 1
                step1 = 0
            elif splittedLines[lineCount][spotCount - step1] == 'L':
                endReached += 1
                step1 = 0
            elif splittedLines[lineCount][spotCount - step1] == '.':
                step1 +=1
            elif step1 > 0:
                step1 = 0
                endReached += 1
        if step2 > 0:
            if splittedLines[lineCount][spotCount + step2] == '#':
                adjacentCount += 1
                endReached += 1
                step2 = 0
            elif splittedLines[lineCount][spotCount + step2] == 'L':
                endReached += 1
                step2 = 0
            elif splittedLines[lineCount][spotCount + step2] == '.':
                step2 +=1
            elif step2 > 0:
                step2 = 0
                endReached += 1
        if step3 > 0:
            if splittedLines[lineCount - step3][spotCount - step3] == '#':
                adjacentCount += 1
                endReached += 1
                step3 = 0
            elif splittedLines[lineCount - step3][spotCount - step3] == 'L':
                endReached += 1
                step3 = 0
            elif splittedLines[lineCount - step3][spotCount - step3] == '.':
                step3 +=1
                
            elif step3 > 0:
                step3 = 0
                endReached += 1
        if step4 > 0:
            if splittedLines[lineCount - step4][spotCount + step4] == '#':
                adjacentCount += 1
                endReached += 1
                step4 = 0
            elif splittedLines[lineCount - step4][spotCount + step4] == 'L':
                endReached += 1
                step4 = 0
            elif splittedLines[lineCount - step4][spotCount + step4] == '.':
                step4 +=1     
            elif step4 > 0:
                step4 = 0
                endReached += 1
        if step5 > 0:
            if splittedLines[lineCount + step5][spotCount - step5] == '#':
                adjacentCount += 1
                endReached += 1
                step5 = 0
            elif splittedLines[lineCount + step5][spotCount - step5] == 'L':
                endReached += 1
                step5 = 0
            elif splittedLines[lineCount + step5][spotCount - step5] == '.':
                step5 +=1 
            elif step5 > 0:
                step5 = 0
                endReached += 1
        if step6 > 0:
            if splittedLines[lineCount + step6][spotCount + step6] == '#':
                adjacentCount += 1
                endReached += 1
                step6 = 0
            elif splittedLines[lineCount + step6][spotCount + step6] == 'L':
                endReached += 1
                step6 = 0
            elif splittedLines[lineCount + step6][spotCount + step6] == '.':
                step6 +=1
            elif step6 > 0:
                step6 = 0
                endReached += 1
        if step7 > 0:
            if splittedLines[lineCount - step7][spotCount] == '#':
                adjacentCount += 1
                endReached += 1
                step7 = 0
            elif splittedLines[lineCount - step7][spotCount] == 'L':
                endReached += 1
                step7 = 0
            elif splittedLines[lineCount - step7][spotCount] == '.':
                step7 +=1
            elif step7 > 0:
                step7 = 0
                endReached += 1
        if step8 > 0:
            if splittedLines[lineCount + step8][spotCount] == '#':
                adjacentCount += 1
                endReached += 1
                step8 = 0
            elif splittedLines[lineCount + step8][spotCount] == 'L':
                endReached += 1
                step8 = 0
            elif splittedLines[lineCount + step8][spotCount] == '.':
                step8 +=1
            elif step8 > 0:
                step8 = 0
                endReached += 1

    if adjacentCount > acceptedOccupied:
        return False
    else:
        return True
    

def ChangeSeating(splittedLines):
    changedSeating = 0  
    lineCount = 0
    spotCount = 0
    newLines = copy.deepcopy(splittedLines)

    for line in splittedLines:
        for spot in line:
            if spot == 'L':
                acceptedOccupied = 0
                if CheckSeatsInSight(newLines, lineCount, spotCount, acceptedOccupied):
                    splittedLines[lineCount][spotCount] = '#'
                    changedSeating += 1
            elif spot == '#':
                acceptedOccupied = 4
                if not CheckSeatsInSight(newLines, lineCount, spotCount, acceptedOccupied):
                    splittedLines[lineCount][spotCount] = 'L'
                    changedSeating += 1
            spotCount += 1
        spotCount = 0
        lineCount += 1
    return changedSeating, splittedLines


def main(lines):
    paddedLines = PadLines(lines)
    splittedLines = convert2Array(paddedLines)
    while True:
        
        changedSeating, changedLines = ChangeSeating(splittedLines)
        newLines = copy.deepcopy(splittedLines)
        if changedSeating == 0:
            occupied = CountOccupied(changedLines)
            print(occupied)
            return occupied

        
main(lines)