weather = (1, 0, 0, 0, 1, 1, 0)
rainy = weather.count(1)
sunny = weather.count(0)

print(rainy)
print(sunny)

if rainy > sunny:
    print("Prediction: Rainy Weather")
else:
    print("Prediction: Sunny Weather")
