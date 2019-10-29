Hero_num = int(input("How many heroes must we gather?"))
print(Hero_num)
print("Gathering heroes…")

count = 1

while count <= Hero_num:
    print("...found hero", count)
    count = count + 1
print("...all the heroes have been gathered")