number1 = int(input("please enter a whole number: "))
number2 = int(input("please enter a second whole number: "))
number3 = int(input("please enter a third whole number: "))

moduloNumber1 = number1 % 2
moduloNumber2 = number2 % 2
moduloNumber3 = number3 % 2

even = 0
odd = 0

if moduloNumber1 == 0:
    even += 1
else:
    odd += 1
if moduloNumber2 == 0:
    even += 1
else:
    odd += 1
if moduloNumber3 == 0:
    even += 1
else:
    odd += 1

print("There were " + str(even) + " even and " + str(odd) + " odd numbers.")