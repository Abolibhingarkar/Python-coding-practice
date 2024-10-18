def hotel_cost(nights): #defines hotel cost based on nights stayed
  return 140 * nights


def plane_ride_cost(city): #defines plane ride cost based on destination city
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475


def rental_car_cost(days): #defines rental car cost based on days rented, discount is offered 
  cost = 40 * days
  return cost
  if days >= 7:
    return cost - 50
  elif days >= 3:
    return cost - 20


def trip_cost(city, days, spending_money): #calculating entire trip cost and accounting for any additional costs
  return hotel_cost(days-1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money