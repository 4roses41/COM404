charged = int(input("how many bars should be charged? "))
print(charged)

bars = "" 

while charged > 0:
    bars += "█ "
    print("Charging: " + bars )
    charged -= 1