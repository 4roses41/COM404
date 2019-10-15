#sum of weights calculation
def SumWeights(Bop, Beep):
    answer = Bop + Beep
    return answer
#average of weights calculation
def calcAvgWeight(Bop, Beep):
    answer = SumWeights(Bop, Beep) / 2
    return answer

# Main question 
def run():
    Bop = int(input("Please enter the weight for Bop: "))  #inputs
    Beep = int(input("Please enter the weight of Beep: "))  #inputs
    SumOrAverage = input("would you like to sum or average? ") #inputs
    if SumOrAverage == "sum":
        print("the sum of the weights is " + str(SumWeights(Bop, Beep))) #make sure to remember to call back to the input values 
    elif SumOrAverage == "average":
        print("the average of the weights is " + str(calcAvgWeight(Bop, Beep))) #also remember to call on the previous functions i.e sum average
    else:
        print("could not calculate")

#remember to call on the main / run function        
run()
