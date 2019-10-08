word = input("Please enter a phrase: ")
print(word)

lettercount = int(len(word))

while lettercount > 0:
    print("Bop " * lettercount)
    lettercount -= lettercount