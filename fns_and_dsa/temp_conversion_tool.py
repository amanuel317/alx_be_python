FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
      return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = float(input("Enter the temperature to convert: "))
typewhat = input("Is this temperature in Celsius or Fahrenheit? (C/F):""Is this temprature in Celsius or Fahrenheit? (C/F): ")


if typewhat == 'F':
    temp_converted=convert_to_fahrenheit(temp)
    print(f'{temp}°F is {temp_converted}°C')
elif typewhat == 'C':
    temp_converted = convert_to_celsius(temp)
    print(f'{temp}°C is {temp_converted}°F')
else:
    print("Invalid temperature. Please enter a numeric value.")
        