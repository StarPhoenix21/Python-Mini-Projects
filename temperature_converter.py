def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    print("Temperature Unit Converter")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius = {celsius_to_fahrenheit(celsius)} Fahrenheit")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit = {fahrenheit_to_celsius(fahrenheit)} Celsius")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius = {celsius_to_kelvin(celsius)} Kelvin")
    elif choice == '4':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin = {kelvin_to_celsius(kelvin)} Celsius")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
