health = 100
print("Your health is 100%. Escape is in progress... ")

for question in range(5):
    response = input("…Oh dear, who is that? ")
    print(response)
    if response == "Smiler's Bot":
        health -= 20
        print("Time to jam out of here!")
    elif response == "hacker":
        health += 20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")
print("Escaped! Health is", str(health) + "%")
    