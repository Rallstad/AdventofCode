from utils import readFile
import re

lines = readFile('inputs/inputTask16.txt')

def GetValidRanges(lines):
    valids = []
    rangeMinMax = []
    for line in lines:
        if re.findall('your ticket', line):
            break
        elif line == '':
            continue
        else:
            line = line.split(':')
            ranges = line[1].split('or')

            for r in ranges:
                r = r.strip()
                rangeMinMax = r.split('-')

                for num in range(int(rangeMinMax[0]), int(rangeMinMax[1])+1):
                    
                    if num not in valids:
                        valids.append(num)
    return valids

def GetNearbyTicketList(lines):
    get_lines = False
    nearbyTicketsList = []

    for line in lines:
        if line.startswith('nearby tickets:'):
            get_lines = True
            continue

        if get_lines:
            splitline = line.split(',')
            nearbyTicketsList.append(splitline)

    return nearbyTicketsList


def CalcTicketErrorRate(lines): #it is importaint to choose good names for yourself
    errorRate = 0
    valids = GetValidRanges(lines)
    nearbyTicketsList = GetNearbyTicketList(lines)

    for nearbyTicket in nearbyTicketsList:
        for num in nearbyTicket:
            if int(num) not in valids:
                print(num)
                errorRate += int(num)

    return errorRate

# part b

def GetValidTickets(lines, valids):
    nearbyTicketsList = GetNearbyTicketList(lines)
    for nearbyTicket in nearbyTicketsList:
        for num in nearbyTicket:
            if int(num) not in valids:
                nearbyTicketsList.remove(nearbyTicket)
    print("nearbyTicketsList")
    print(nearbyTicketsList)
    return nearbyTicketsList


# list fields and their ranges
def ListFieldRanges(lines):
    validsList = []
    tmp = []

    for line in lines:
        if re.findall('your ticket', line):
            break
        elif line == '':
            continue
        else:
            line = line.split(':')
            ranges = line[1].split('or')

            for r in ranges:
                r = r.strip()
                rangeMinMax = r.split('-')
                tmp.append(line[0])
                for num in range(int(rangeMinMax[0]), int(rangeMinMax[1])+1):
                    tmp.append(num)
            validsList.append(tmp)
            tmp = []
        
    print(validsList)
    return validsList



def MultiplyDepartureNumbers(lines): #it is importaint to choose good names for yourself
    nearbyTicketsList = GetNearbyTicketList(lines)
    valids = GetValidRanges(lines)
    validNearbyTickets = GetValidTickets(lines, valids)
    validsList = ListFieldRanges(lines)

    inRange = True
    fields = [0]*20
    count = 0
    
    for i in range(0, len(validsList)):
        for c in range(len(nearbyTicketsList)):
            if inRange == True:
                break
            for nearbyTicket in nearbyTicketsList:
                if count == 20:
                    count = 0
                    inRange = True
                    break
                elif int(nearbyTicket[count]) not in validsList[i]:
                    inRange == False
                    break
            

            if inRange == True:
                print(validsList[i][0])
                fields.append(validsList[i][0])
            inRange = False
            count = 0
            
    print(fields)
    return fields
            
print(MultiplyDepartureNumbers(lines))
#print(CalcTicketErrorRate(lines))




