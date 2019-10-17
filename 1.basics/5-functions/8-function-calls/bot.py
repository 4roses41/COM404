def DisplayInBox(CrypWord):
    print("*" * (len(CrypWord) + 10))
    print("**  ", CrypWord, "  **")
    print("*" * (len(CrypWord) + 10))

def DisplayLowerCase(CrypWord):
    answer =  (CrypWord.lower())
    return answer 

def DisplayUpperCase(CrypWord):
    answer =  (CrypWord.upper())
    return answer 

def DisplayMirrored(CrypWord):
    print()

def Repeat(Crypword):
    Howmany = int(input("How many times would you like to repeat the word? "))
    answer = Crypword * Howmany
    return answer
  
def Run():
    CrypWord = input("Please enter a Word: ")
    print(" 1) Display in a Box \n 2) Display Lower-case \n 3) Display Upper-case \n 4) Display Mirrored \n 5) Repeat  ")
    whatToHappen = input("please enter What you would like to happen to the word (1, 2, 3, 4, 5): ")
    if whatToHappen == "1":
        DisplayInBox(CrypWord)
    elif whatToHappen == "2":
        print(DisplayLowerCase(CrypWord))
    elif whatToHappen == "3":
        print(DisplayUpperCase(CrypWord))
    elif whatToHappen == "4":
        print(DisplayMirrored(CrypWord))
    elif whatToHappen == "5":
        print(Repeat(CrypWord))
    else:
        print("please enter another word and select one of the above options")
    

Run()
