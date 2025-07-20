weather = input(
    "What's the weather like today? (sunny/rainy/cold): ").strip().lower()

if weather == "sunny":
    message = "wear a t-shirt and sun glasses."
elif weather == "rainny":
    message = "Don't forget your umbrella and raincoat."
elif weather == "cold":
    message = "Make sure to wear a warm coat"
else:
    message = " Sorry I don't have recommendations for this weather"
print(message)
