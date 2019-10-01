whereToLook = input("Where should I look? (bedroom/ bathroom /lab): ")
print(whereToLook)

if whereToLook == "bedroom":
    whereInBedroom = input("Where in the bedroom should I look?")
    if whereInBedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")
if whereToLook == "bathroom":
    whereInBathroom = input("Where in the bathroom should I look?")
    if whereInBathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")
if whereToLook == "lab":
    whereInlab = input("Where in the lab should I look?")
    if whereInlab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")