howmanyToSum = int(input("How many numbers should I sum up "))
print(howmanyToSum)

SumOfNumbers = 0
total = 1
numtotal = 0

while total <= howmanyToSum:
    SumOfNumbers = int(input("Please enter number " + str(total) + " of " + str(howmanyToSum) + ": "))
    total += 1
    numtotal += SumOfNumbers

print(numtotal)