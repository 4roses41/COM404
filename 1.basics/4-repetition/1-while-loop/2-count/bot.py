liveCables = int(input("How many live cables must I avoid? "))
print(liveCables)

count = 0

while liveCables > 0:
    count = count + 1 
    print("Avoiding done ... " + str(count) + " live cables avoided.")
    liveCables -= 1 