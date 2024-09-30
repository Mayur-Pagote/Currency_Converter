import easygui  # Import EasyGUI for creating graphical user interfaces
import requests  # Import requests to make HTTP requests

# Set your API key for the exchange rate service
api_key = 'b2e9dd9a31cddf3ecafe303b'

# Prompt the user to enter currency details using a multi-entry dialog
details = easygui.multenterbox("Enter currency details:", "Exchange Rates Calculator", 
          ["Source currency (e.g., USD)", "Conversion currency (e.g., INR)", "Amount (e.g., 10)"])

# Get the source and conversion currencies from the user input and convert to uppercase
source_currency = details[0].upper()
conversion_currency = details[1].upper()

# Convert the amount to float; this assumes the input is valid
amount = float(details[2])

# Construct the URL for the API request to get the latest exchange rates
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}'

# Make the API request to fetch exchange rates
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the response JSON
    conversion_rates = data["conversion_rates"]  # Extract conversion rates

    # Check if the desired conversion currency exists in the rates
    if conversion_currency in conversion_rates:
        # Calculate the converted amount and display it in a message box
        easygui.msgbox(f"Converted amount is {(amount) * conversion_rates[conversion_currency]} {conversion_currency}")
    else:
        # Inform the user if the conversion currency is invalid
        easygui.msgbox("Invalid data entered.")
