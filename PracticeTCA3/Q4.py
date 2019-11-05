def isFusionShot(slug1, slug2):
    if slug1 == slug2:
        return True
    else:
        return False

def isDefectiveShot(slug1, slug2):
    if isFusionShot(slug1, slug2) == False:
        if slug1 and slug2 == "Infurnus" and "AquaBeek" or "AquaBeek" and "Infurnus":
            return True
    else:
        return False

def run():
    slug1 = input("what is the type of the first slug? ")
    slug2 = input("what is the type of the second slug? ")
    f_or_d = input("input is the slug fusion or defective ")
    if f_or_d == "fusion":
        print(isFusionShot(slug1, slug2))
    elif f_or_d == "defective":
        print(isDefectiveShot(slug1, slug2))
    else:
        print("Invalid selection. Please try again")

run()

