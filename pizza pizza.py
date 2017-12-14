print("Let's see how cost effective getting a large pizza vs a smaller size is:")
pizzaSize1 = input("how many inches is the smaller pizza?")
pizzaPrice1 = float(input("how much is that size?"))

pizzaSqin1 = 3.1415926 * (int(pizzaSize1)/2)**2
pizzaPPSqIn1 = int(pizzaPrice1) / int(pizzaSqin1)

print("That pizza is " + str(round(pizzaSqin1)) + " Sq. inches")
print("Or " + str(round(pizzaPPSqIn1,3)) + " Cents per Sq. inch.")

print()
pizzaSize2 = input("how many inches is the larger pizza?")
pizzaPrice2 = float(input("how much is that size?"))
pizzaSqin2 = 3.1415926 * (int(pizzaSize2)/2)**2
pizzaPPSqIn2 = int(pizzaPrice2) / int(pizzaSqin2)

print("That pizza is " + str(round(pizzaSqin2)) + " Sq. inches")
print("Or " + str((round(pizzaPPSqIn2,3))) + " Cents per Sq. inch.")


pizzaDif = pizzaSqin2 - pizzaSqin1
pizzaSizeDif= pizzaPPSqIn1 - pizzaPPSqIn2


print()
print("The larger pizza is " + str(round(pizzaDif,3)) + " Sq. inches larger than the smaller one")
print("And " + str(round(pizzaSizeDif,5)) + " Per Sq. inch cheaper!")


percentageSize = (pizzaSqin2 - pizzaSqin1) / pizzaSqin1 * 100
percentagePrice = (pizzaPrice2 - pizzaPrice1) / pizzaPrice1 * 100

print("You are getting " + str(round(percentageSize,3)) + " Percent more pizza,")
print("for only " + str(round(percentagePrice,3)) + " Percent more price!")




