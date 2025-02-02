import requests

def get_exchange_rate(from_currency, to_currency):
    """ Fetches exchange rate from an API """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['rates'].get(to_currency, None)
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

def convert_currency(amount, from_currency, to_currency):
    """ Converts the amount using real-time exchange rates """
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def main():
    """ Command-Line Interface for the Currency Converter """
    print("\n🌍 Welcome to the Currency Converter 🌍")
    print("=====================================")
    
    try:
        amount = float(input("\nEnter the amount to convert: "))
        from_currency = input("Enter the source currency (e.g., USD): ").upper()
        to_currency = input("Enter the target currency (e.g., EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        if result:
            print(f"\n💰 {amount:.2f} {from_currency} = {result:.2f} {to_currency} 💰")
        else:
            print("\n❌ Error: Unable to fetch exchange rate. Please check your currency codes.")
    except ValueError:
        print("\n❌ Invalid amount. Please enter a numeric value.")

if __name__ == "__main__":
    main()

