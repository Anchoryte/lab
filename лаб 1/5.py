km = float(input())
expenditure_fuel_liters = float(input())
cost_fuel_liter = float(input())

fuel_per_trip = (km * expenditure_fuel_liters) / 100
cost_trips = fuel_per_trip * cost_fuel_liter

print(f"Топливо: {fuel_per_trip:.2f}")
print(f"Стоимость: {cost_trips:.2f}")









#km = 250
#rashod = 7.5
#sale = 60
#fail = (km * rashod) / 100
#cena = fail * sale
#print(cena)