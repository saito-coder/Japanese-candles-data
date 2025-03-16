import requests
import csv

print('____________________________________________________________')
print(' ')
api_key = 'Q1LSZYK1UER1H7Z7'

print('input your strock symbol')
user_symbol = input()
s_ymbol = str(user_symbol)
symbol = s_ymbol
print(' ')

# Get user input for the function
function = input("Enter the function (e.g., TIME_SERIES_DAILY, TIME_SERIES_INTRADAY): ")
print(' ')

# Define the base URL
url = 'https://www.alphavantage.co/query'

# Define the parameters based on the function
params = {
    'function': function,
    'symbol': symbol,
    'apikey': api_key
}

# Add additional parameters based on the function
if function == 'TIME_SERIES_INTRADAY':
    interval = input("Enter the interval (e.g., 1min, 5min, 15min, 30min, 60min): ")
    params['interval'] = interval

r = requests.get(url, params=params)
data = r.json()

# Extract the time series data
if function == 'TIME_SERIES_DAILY':
    time_series = data.get('Time Series (Daily)', {})
elif function == 'TIME_SERIES_INTRADAY':
    time_series = data.get(f'Time Series ({interval})', {})
else:
    print("Unsupported function")
    time_series = {}

print("name the file .. don't forget the  .csv")
csv_name = input()
csv_f = str(csv_name)
# Define the CSV file name
csv_file = csv_f
print(" ")
# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    # Write the data
    for date, daily_data in time_series.items():
        writer.writerow([
            date,
            daily_data['1. open'],
            daily_data['2. high'],
            daily_data['3. low'],
            daily_data['4. close'],
            daily_data['5. volume']
        ])

print(f"Data has been written to {csv_file}")

# While loop to input date and get stock data
while True:
    input_date = input("Enter the date (YYYY-MM-DD) or 'exit' to quit: ")
    if input_date.lower() == 'exit':
        break
    if input_date in time_series:
        daily_data = time_series[input_date]
        print(f"Date: {input_date}")
        print(f"Open: {daily_data['1. open']}")
        print(f"High: {daily_data['2. high']}")
        print(f"Low: {daily_data['3. low']}")
        print(f"Close: {daily_data['4. close']}")
        print(f"Volume: {daily_data['5. volume']}")
    else:
        print("Data for the entered date is not available.")
        
