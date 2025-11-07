#Diesel car details

diesel_car_price = int(input("Enter Diesel car price : "))
diesel_price_per_litre = 95
average_per_litre = 20
lifespan_of_diesel_car = 15

#electric car details

electric_car_price = int(input("Enter Electric car price : "))
electricity_price_per_unit = 5
average_per_unit = 6
lifespan_of_electric_car = 10

usage_per_month = 5000

#Total distance travelled in lifespan by cars
distance_travelled_bydiesel_car = usage_per_month * 12 * lifespan_of_diesel_car
distance_travelled_byelectric_car = usage_per_month * 12 * lifespan_of_electric_car

#cost per km
diesel_cost_per_km = diesel_price_per_litre / average_per_litre
electricity_cost_per_km = electricity_price_per_unit / average_per_unit

#cars total running cost 
diesel_car_running_cost = diesel_cost_per_km * distance_travelled_bydiesel_car
electric_car_running_cost = electricity_cost_per_km * distance_travelled_byelectric_car


#total cost until lifespan 
diesel_car_total_cost = diesel_car_price + diesel_car_running_cost
electric_car_total_cost = electric_car_price + electric_car_running_cost


print("++++++++++++++++++++")
print("Diesel car Details")
print("Diesel car price : ",diesel_car_price)
print("Diesel car Running cost : ", diesel_car_running_cost)
print("Distance Travelled by Diesel car : ", distance_travelled_bydiesel_car)
print("Diesel car total cost till lifespan : ",diesel_car_total_cost)
print("++++++++++++++++++++")

print("++++++++++++++++++++")
print("Electric car Details ")
print("Eletric car price : ",electric_car_price)
print("Electric car Running cost : ", electric_car_running_cost)
print("Distance Travelled by Electric car : ", distance_travelled_byelectric_car)
print("Electric car total cost till lifespan : ",electric_car_total_cost)
print("++++++++++++++++++++")

if diesel_car_total_cost > electric_car_total_cost:
	print("Electric car is better.")
else :
	print("Diesel car is better.")