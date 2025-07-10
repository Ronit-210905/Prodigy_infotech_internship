def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

print("Welcome to Temperature Converter!")
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

if unit == "C":
    print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
    print(f"{temp}°C is {celsius_to_kelvin(temp):.2f}K")

elif unit == "F":
    print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
    print(f"{temp}°F is {fahrenheit_to_kelvin(temp):.2f}K")

elif unit == "K":
    print(f"{temp}K is {kelvin_to_celsius(temp):.2f}°C")
    print(f"{temp}K is {kelvin_to_fahrenheit(temp):.2f}°F")

else:
    print("Invalid unit entered. Please use C, F, or K.")
