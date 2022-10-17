# 2. Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.
print("\nWelcome to the trip cost calculator!")
distance = float(input("Distance of the trip [km]: "))
consumption = float(input("Fuel consumption per 100km [l]: "))
fuel_price = float(input("Fuel price per litre [zł]: "))
print("The trip will cost:", round(((distance / 100) * consumption * fuel_price), 2), "PLN")
