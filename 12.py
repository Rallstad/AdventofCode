from utils import readFile
import re

instructions = readFile('inputs/inputTask12.txt')

#I must say, this way of writing function and variable names, I do not like



def RotateShip(pos, command, magnitude, newDirection):   
    if command == 'L':
        magnitude = -magnitude
    newDirection = (newDirection + magnitude) % 360
    pos.update({'F':newDirection})

    return newDirection

def RotateWaypoint(waypoint, command, magnitude, newDirection):
    if command == 'L':
        magnitude = -magnitude

    if magnitude == 90 or magnitude == -270:
        tmpE = waypoint['E']
        tmpS = waypoint['S']
        tmpW = waypoint['W']
        tmpN = waypoint['N']
        
        waypoint.update({'S':tmpE})
        waypoint.update({'W':tmpS})
        waypoint.update({'N':tmpW})
        waypoint.update({'E':tmpN})

        return waypoint

    if magnitude == 180 or magnitude == -180:
        tmpE = waypoint['E']
        tmpS = waypoint['S']
        tmpW = waypoint['W']
        tmpN = waypoint['N']

        waypoint.update({'E':tmpW})
        waypoint.update({'N':tmpS})
        waypoint.update({'W':tmpE})
        waypoint.update({'S':tmpN})

        return waypoint

    if magnitude == 270 or magnitude == -90:
        tmpE = waypoint['E']
        tmpS = waypoint['S']
        tmpW = waypoint['W']
        tmpN = waypoint['N']

        waypoint.update({'E':tmpS})
        waypoint.update({'S':tmpW})
        waypoint.update({'W':tmpN})
        waypoint.update({'N':tmpE})

        return waypoint

    return waypoint


def MoveInCommandDirection(pos, command, magnitude):
    pos[command] += magnitude

def UpdateWaypoint(waypoint, command, magnitude):
    waypoint[command] += magnitude

    return waypoint

def MoveForwardByWaypoint(actualPos, command, magnitude, waypoint):
    actualPos['E'] += magnitude * waypoint['E']
    actualPos['S'] += magnitude * waypoint['S']
    actualPos['W'] += magnitude * waypoint['W']
    actualPos['N'] += magnitude * waypoint['N']

def MoveForwardInCurrentDirection(pos, command, magnitude):
    if pos['F'] == 0:
        pos['E'] += magnitude
    elif pos['F'] == 90:
        pos['S'] += magnitude
    elif pos['F'] == 180:
        pos['W'] += magnitude
    elif pos['F'] == 270:
        pos['N'] += magnitude


def GetShipPos(instructions):
    directions = [0, 90, 180, 270] # from left to right: E S W N
    pos = {'E':0, 'S':0, 'W':0, 'N':0, 'F':0} # F is current heading
    actualPos = {'E':0, 'S':0, 'W':0, 'N':0, 'F':0}
    waypoint = {'E':1, 'S':0, 'W':0, 'N':1, 'F':0} # F is current heading. Value is units

    shipDirection = pos['F']
    newDirection = 0

    for instruction in instructions:
        command = instruction[0]
        magnitude = int(re.findall('[0-9]+', instruction)[0])

        if command == 'F':
            MoveForwardByWaypoint(actualPos, command, magnitude, waypoint)
            MoveForwardInCurrentDirection(pos, command, magnitude)
        elif command in pos:
            MoveInCommandDirection(pos, command, magnitude)
            waypoint = UpdateWaypoint(waypoint, command, magnitude)
        elif command not in pos.keys():
            waypoint = RotateWaypoint(waypoint, command, magnitude, newDirection)
            newDirection = RotateShip(pos, command, magnitude, newDirection)
    
    totalWaypoint = abs(actualPos['E'] - actualPos['W']) + abs(actualPos['S'] - actualPos['N'])
    totalShipPos = abs(pos['E'] - pos['W']) + abs(pos['S'] - pos['N'])

    return totalWaypoint, totalShipPos

print(GetShipPos(instructions))

            

        




