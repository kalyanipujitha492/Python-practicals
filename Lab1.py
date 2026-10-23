def fahrenheit_to_celsius(fahrenheit):

return (fahrenheit - 32) *5.0/9.0

def celsius_to_fahrenheit(celsius):

return (celsius 9/5 )+32

def main():

while True:

print("\nTemperature Conversion Menu:")

print("1. Convert Fahrenheit to Celsius")

print("2. Convert Celsius to Fahrenheit")

print("3. Exit")

choice = input("Enter your choice ((1/2) / 3) ")

if choice ==^ prime 1'

f = float(input("Enter temperature in Fahrenheit: ")

c = fahrenheit_to_celsius(f)

print(f"{f:.2f}°F is equal to (c:.2f}°C")

elif choice ==^ prime 2'

c = float(input("Enter temperature in Celsius: "))

f = celsius_to_fahrenheit(c)

print(f"{c:.2f}°C is equal to \{f / 0.2 * f\} deg F^ prime prime )

elif choice ==^ prime 3' :

print("Exiting program. Goodbye!")

break

-d

d.

else:

print("Invalid choice. Please enter 1, 2, or 3.")

if main() \ name\ ==\ main\ ^ prime
