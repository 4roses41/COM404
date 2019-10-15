def crossBridge(HowFar):
    for steps in range(HowFar):
        print("crossed step")
    if HowFar > 5:
        print("we must keep going")
    else:
        print("the bridge is colapsing! ")
crossBridge(3)
crossBridge(6)

