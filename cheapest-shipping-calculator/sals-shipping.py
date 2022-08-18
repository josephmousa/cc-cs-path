#change the weight value here to compare the prices for each shipping method based on this weight
weight = 41.5

#Ground Shipping
cost = 20
if weight <= 2:
  cost += (weight * 1.5)
elif weight > 2 and weight <= 6:
  cost += (weight * 3)
elif weight > 6 and weight <= 10:
  cost += (weight * 4)
else:
  cost += (weight * 4.75)

print("Ground shipping cost: ", cost)

premium_cost = 125
print("Premium shipping cost ", premium_cost)

#Drone Shipping
cost_drone = 0
if weight <= 2:
  cost_drone += (weight * 4.5)
elif weight > 2 and weight <= 6:
  cost_drone += (weight * 9)
elif weight > 6 and weight <= 10:
  cost_drone += (weight * 12)
else:
  cost_drone += (weight * 14.25)

print("Drone shipping cost: ", cost_drone)
