# Import required libraries
from forex_python.converter import CurrencyRates

# Create a CurrencyRates object to fetch exchange rates
c = CurrencyRates()

# Define a function for currency conversion
def currency_converter():
    # Get user input for the amount to convert
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get user input for source and target currencies
    source_currency = input("Enter the source currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()

    # Get the exchange rate and perform the conversion
    exchange_rate = c.get_rate(source_currency, target_currency)
    converted_amount = amount * exchange_rate

    # Display the result
    print(f"{amount} {source_currency} is equal to {converted_amount} {target_currency}")
    print(f"Exchange rate used: 1 {source_currency} = {exchange_rate} {target_currency}")

if __name__ == "__main__":
    print("Welcome to the Currency Converter!")
    while True:
        currency_converter()
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != "yes":
            break
    print("Thank you for using the Currency Converter!")
