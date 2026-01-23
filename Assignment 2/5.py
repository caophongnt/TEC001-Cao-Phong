import math
def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = math.pi * radius ** 2
    area_m2 = area_cm2 / 10000
    return price / area_m2
d1 = float(input("Enter diameter of first pizza (cm): "))
p1 = float(input("Enter price of first pizza (USD): "))
d2 = float(input("Enter diameter of second pizza (cm): "))
p2 = float(input("Enter price of second pizza (USD): "))
up1 = pizza_unit_price(d1, p1)
up2 = pizza_unit_price(d2, p2)
if up1 < up2:
    print("The first pizza provides better value for money.")
elif up2 < up1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas have the same value for money.")