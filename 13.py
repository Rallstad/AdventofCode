from utils import readFile

departures = readFile('inputs/inputTask13.txt')


def GetEarliestDeparture(departures):
    currentTimestamp = departures[0]
    departures = departures[1].split(',')

    earliestDeparture = float('inf')
    afterCurrentTimestamp = 0

    for departure in departures:
        if departure != 'x':
            departure = int(departure)
            while afterCurrentTimestamp <= int(currentTimestamp):
                afterCurrentTimestamp += departure
            if afterCurrentTimestamp < earliestDeparture:
                earliestDeparture = afterCurrentTimestamp
                buss2Take = departure
            afterCurrentTimestamp = 0
    num = (earliestDeparture - int(currentTimestamp)) * buss2Take
    return num

def FindFirstDeparturesInSequence(departures):

    departures = departures[1].split(',')
    earliestDeparture = float('inf')
    afterCurrentTimestamp = 0
    index = []
    sequence = 0
    timestamp = 0
    

    #populate index to find departures times that are not 'x'
    count = 0
    for departure in range(len(departures)):
        if departures[departure] != 'x':
            index.append(departure)
            count += 1
        else:
            index.append(-1)
    print(count)
    inSequence = 1
    multiplier = 1
    timestamp = 100000000000000
    reqAcc = False
    
    while reqAcc == False:
        inSequence = 1

        timestamp += int(departures[0])
 
        iCount = 1
        for i in index[1:]: 
            if i != -1:
                if (timestamp + index[iCount]) % int(departures[iCount]) == 0:
                    inSequence += 1
            iCount += 1
        if inSequence == count:
            reqAcc = True

        #inSequence = 1
    timestamp += int(departures[0])
    return timestamp

#print(GetEarliestDeparture(departures))
print(FindFirstDeparturesInSequence(departures))


