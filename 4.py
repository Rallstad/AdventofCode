from utils import readFile
import re

lines = readFile('inputs/inputTask4.txt')

def getPassportsWithCorrectElements(lines):
    values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport = []
    count = 0
    validPassports = 0

    for line in lines:
        if line:
            for word in line.split():
                passport.append(word)
        else:
            for elem in passport:
                if elem.split(':')[0] in values:
                    count = count + 1
            if count >= len(values):
                validPassports = validPassports + 1

            count = 0
            passport = []

    for elem in passport:
        if elem.split(':')[0] in values:
            count = count + 1
    if count >= len(values):
        validPassports = validPassports + 1
    count = 0
    passport = []

    return validPassports


def checkIfValidPassport(passport):
    validEntries = 0
    values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    for elem in passport:
        
        entry = elem.split(':')[0]
        entryValue = elem.split(':')[1]

        if entry == 'byr':
            if 1920 <= int(entryValue) <= 2002:
                validEntries = validEntries + 1

        elif entry == 'iyr':
            if 2010 <= int(entryValue) <= 2020:
                validEntries = validEntries + 1

        elif entry == 'eyr':
            if 2020 <= int(entryValue) <= 2030:
                validEntries = validEntries + 1

        elif entry == 'hgt':
            if re.search('cm$', entryValue):
                num = re.findall('[0-9]{1,3}', entryValue)
                if 150 <= int(num[0]) <= 193:
                    validEntries = validEntries + 1

            elif re.search('in$', entryValue):
                num = re.findall('[0-9]{1,3}', entryValue)
                if 59 <= int(num[0]) <= 76:
                    validEntries = validEntries + 1

        elif entry == 'hcl':
            if entryValue[0] == "#" and re.findall('[a-z0-9]', entryValue.split('#')[1]) and len(entryValue.split('#')[1]) == 6:
                validEntries = validEntries + 1

        elif entry == 'ecl':
            if entryValue in eyeColor:
                validEntries = validEntries + 1

        elif entry == 'pid':
            if re.match("[0-9]", entryValue) and len(entryValue) == 9:
                validEntries = validEntries + 1
        
        else:
            continue 

        if validEntries >= len(values):
            return 1

    return 0



def getPassportsWithValidValues(lines):
    passport = []
    validPassports = 0

    for line in lines:
        if line:
            for word in line.split():
                passport.append(word)
        else:
            if len(passport) < 7:
                passport = []
                continue

            if checkIfValidPassport(passport):
                validPassports = validPassports + 1

            passport = []

    return validPassports

#getPassportsWithCorrectElements(lines)       
print(getPassportsWithCorrectElements(lines))

#getPassportsWithValidValues(lines)       
print(getPassportsWithValidValues(lines))