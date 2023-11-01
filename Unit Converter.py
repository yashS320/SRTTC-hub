def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("Welcome to the Temperature Converter!")
        print("Select an option:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3): "))
            
            if choice == 3:
                print("Goodbye!")
                break
            elif choice not in (1, 2):
                print("Invalid choice. Please select 1, 2, or 3.")
                continue

            value = float(input("Enter the temperature value: "))

            if choice == 1:
                result = celsius_to_fahrenheit(value)
                print(f"{value}°C is equal to {result}°F")
            else:
                result = fahrenheit_to_celsius(value)
                print(f"{value}°F is equal to {result}°C")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
