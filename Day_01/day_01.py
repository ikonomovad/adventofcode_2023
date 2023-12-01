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