
total_human = 0
total_ape = 0

print("Welcome to the Planet of the Apes…")

for question in range(7):
    response = input("…be ye human or be ye ape? ")
    print(response)
    if response == "human":
        total_human = total_human + 1
        print("I did not start this war. But I will finish it.")
    elif response == "ape":
        total_ape = total_ape + 1
        print("Apes together strong!")
    else:
        print("This is not your fight")



print("Total Humans encountered: " + str(total_human))
print("Total apes encountered: " + str(total_ape))

