# part 1

values = []
        
with open('input.txt') as file:
    for line in file:
        integer = ''
        for char in line:
            if char.isdigit():
                integer += char
        values.append(integer[0] + integer[-1])

sum = 0    
for value in values:
    sum += int(value)
    
print(sum)

#part 2

stringNumbers = {
    'one': '1', 
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

formattedLines = []

with open('input.txt') as file:
    for line in file:
        integer = ''
        for ind, char in enumerate(line):
            subString = ''
            if char.isdigit():
                integer += char
            else:
                subString = line[ind:]
                for numAsString, num in stringNumbers.items():
                    if subString.startswith(numAsString):
                        integer += num
        formattedLines.append(integer)
 
values2 = []   

for number in formattedLines:
    newLine = number[0] + number[-1]
    values2.append(newLine)

sum2 = 0    
for value in values2:
    sum2 += int(value)
    
print(sum2)