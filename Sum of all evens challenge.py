# solution 1
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
if numbers[0] % 2 == 0:
    print (numbers)
else:
    del(numbers[0])
    numbers.insert(0, 0)
    
if numbers[1] % 2 == 0:
    print (numbers)
else:
    del(numbers[1])
    numbers.insert(1, 0)
print (numbers)
if numbers[2] % 2 == 0:
    print (numbers)
else:
    del(numbers[2])
    numbers.insert(2, 0)
    
if numbers[3] % 2 == 0:
    print (numbers)
else:
    del(numbers[3])
    numbers.insert(3, 0)
    
if numbers[4] % 2 == 0:
    print (numbers)
else:
    del(numbers[4])
    numbers.insert(4, 0)
    
if numbers[5] % 2 == 0:
    print (numbers)
else:
    del(numbers[5])
    numbers.insert(5, 0)
    
if numbers[6] % 2 == 0:
    print (numbers)
else:
    del(numbers[6])
    numbers.insert(6, 0)
    
if numbers[7] % 2 == 0:
    print (numbers)
else:
    del(numbers[7])
    numbers.insert(7, 0)
    
if numbers[8] % 2 == 0:
    print (numbers)
else:
    del(numbers[8])
    numbers.insert(8, 0)
    
if numbers[9] % 2 == 0:
    print (numbers)
else:
    del(numbers[9])
    numbers.insert(9, 0)
    
print (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7] + numbers[8] + numbers[9])

# solution 2
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
total = 0
for number in numbers:
    if number % 2 == 0:
        total = total + number
        print (total)

# solution 3
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        print (even_numbers)
print (even_numbers[0] + even_numbers[1] + even_numbers[2] + even_numbers[3] + even_numbers[4] + even_numbers[5])