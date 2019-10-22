ZoneToCross = int(input("How many zones must I cross? "))
print(ZoneToCross)

count = ZoneToCross

print("Crossing Zones...")
for cross in range(ZoneToCross):
    print("…crossed zone " + str(ZoneToCross))
    ZoneToCross -= 1
print("Crossed all zones.  Jumanji!")