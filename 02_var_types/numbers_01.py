# 1. Oblicz koszt wyprawy znają̨c dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi
# 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
distance = 120
consumption = 6.4
fuel_price = 5.04
print("The trip will cost:", round(((distance / 100) * consumption * fuel_price), 2), "PLN")
