def under(word):
    print(word)
    print("*" * len(word))

def over(word):
    print("*" * len(word))
    print(word)

def both(word):
    print("*" * len(word))
    print(word)
    print("*" * len(word))

def grid(word, gridSize):
    for star in range(len(word), gridSize):
        print(gridSize * len(word) * " *")
    for name in range(word, gridSize):
        print(int(word) + " |" + len(word) * " " )
    print(int(gridSize) * len(word) * " *") 

   ##print("*" * len(word))
      #  print(word + " |")
  #  print("*" * len(word))

def run():
    word = input("please enter a word ")
    print("Options\n 1) Under \n 2) Over \n 3) Both \n 4) Grid")
    option = str(input("please enter an option to edit the Word(1, 2, 3 or 4): "))
    if option == "1":
        under(word)
    elif option == "2":
        over(word)
    elif option == "3":
        both(word)
    elif option == "4":
        gridSize = int(input("please enter how Large you would like to make the grid "))
        grid(word, gridSize)
    else:
        print("please try again and enter a valid option")
    

run()