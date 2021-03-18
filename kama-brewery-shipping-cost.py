#Kama Brewerys beer shipping cost tablet

print("Kama Brewery's beer shipping")
print("")

print("How many cans:")
amount = 39
print(amount)
print("")

#Ground Shipping by snail mail
if amount <= 10:
  ground_cost = 2.0 * amount + 20
elif amount <= 20:
  ground_cost = 2.5 * amount + 20
elif amount <= 40:
  ground_cost = 4.0 * amount + 20
else:
  ground_cost = 5.0 * amount + 20

print("Ground Shipping:", ground_cost, "€")

premium_ground_shipping = 150
print("Premium Ground Shipping:", premium_ground_shipping, "€")

#Straigth out of brewery
if amount <= 10:
  brewery_cost = 5.0 * amount
elif amount <= 20:
  brewery_cost = 4.0 * amount
elif amount <= 50:
  brewery_cost = 2.0 * amount
else:
  brewery_cost = 1.0 * amount

print("Straight out of brewery:", brewery_cost, "€")
