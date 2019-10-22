def is_league_united(Hero1, Hero2):
    if Hero1 == "Superman" and Hero2 == "WonderWoman" or Hero1 == "WonderWoman" and Hero2 == "Superman":
        return True
    else:
        return False

def decide_plan(Hero1, Hero2):
    if is_league_united(Hero1, Hero2) == True:
        return "Time to save the world! "
    else:
        return "We must unite the league!"

def run():
    Hero1 = input("Please enter the name of a hero: ")
    Hero2 = input("Please enter the name of another hero: ")
    L_or_P = input("Please enter League or Plan: ")
    if L_or_P == "League":
        print(is_league_united(Hero1, Hero2))
    elif L_or_P == "Plan":
        print(decide_plan(Hero1, Hero2))
    else:
        print("Invalid command. Please try again")




run()