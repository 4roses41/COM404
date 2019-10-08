brightness = int(input("What level of brightness is required? "))
print(brightness)

bop = "*"
beep = "*"

for starts in range(2,brightness,2):
    print("Beep's brightness level: " + starts * beep)
    print("Bop's brightness level: " + starts * bop 
    )
print("Adjustments complete!")

