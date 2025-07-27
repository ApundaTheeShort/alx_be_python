FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temprature = float(input("Enter the temprature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()


def convert_to_celcius(fahrenheit):
    converted_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {converted_temp}°C")


def convert_to_fahrenheit(celcius):
    converted_temp = celcius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celcius}°C is {converted_temp}°F")


if isinstance(temprature, int) or isinstance(temprature, float):
    if temp_type == "f":
        convert_to_celcius(temprature)
    elif temp_type == "c":
        convert_to_fahrenheit(temprature)
    else:
        print("Invalid input! ")
else:
    print("Invalid temperature. Please enter a numeric value.")
