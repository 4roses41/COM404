# loop has to be within the function 

def displayLadder(steps):
    for ladder in range(int(steps)):
        print("|  |")
        print("****")
def createLadder():
    steps = int(input("How many steps are on the ladder?"))
    displayLadder(steps)

createLadder()

