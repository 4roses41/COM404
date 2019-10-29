print("Welcome to the Planet of the Apes…")

human = 0
ape = 0

for repeat in range(7):
    question = input("…be ye human or be ye ape?")
    print(question)

    if question == "human":
        print("I did not start this war. But I will finish it")
        human = human +1
    elif question == "ape":
        print("Apes together strong!")
        ape = ape + 1
    else:
        print("This is not your fight.")

print("Total humans encountered:", str(human))
print("Total apes encountered:", str(ape))

