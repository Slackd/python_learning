#! /usr/bin/python3

# Celcius to Fahrenheit Converter
# C to F and F to C functionality

# Function definitions of c2f and f2c
def celciusFahrenheit():
    try:
        celcius = float(input("Enter ^C Temperature:"))
        fahrenheit = ((celcius) * 9 / 5) + (32)
        print("The Temperature is: ", fahrenheit,"^Fahrenheit")
    except:
        print("Please enter a number only!")

def fahrenheitCelcius():
    try:
        fahrenheit = float(input("Enter ^F Temperature:"))
        celcius = ((fahrenheit) - 32) * (5 / 9)
        print("The Temperature is: ", celcius,"^Celcius")
    except:
        print("Please enter a number only!")


# Step 1 : Offer a choice to the user between c>f or f>c
print("1. Convert Celcius to Fahrenheit:")
print("2. Convert Fahrenheit to Celcius:")
print("3. Exit:\n")
option = int(input("Choice>1/2 or 3:"))

if option == 1 :
    celciusFahrenheit()
elif option == 2: 
    fahrenheitCelcius()
else:
    option == 3
    exit()
