def escapeBy(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")
escapeBy("jumping over")
escapeBy("running around")
escapeBy("going deeper")

