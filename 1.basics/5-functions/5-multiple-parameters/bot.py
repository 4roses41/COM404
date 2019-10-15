def ClimbLadder(StepsRemaining, stepsCrossed):
    if StepsRemaining < stepsCrossed:
        print("still some way to go")
    else:
        print("we made it!")
ClimbLadder(2, 5)
ClimbLadder(5, 5)
