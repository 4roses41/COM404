stepsAway = int(input("How far are we from the cave? "))
print(stepsAway)


for steps in range (0,stepsAway,1):
    print(str(stepsAway) + " steps remaining ")
    stepsAway -= 1
print("We have reached the cave!")

    