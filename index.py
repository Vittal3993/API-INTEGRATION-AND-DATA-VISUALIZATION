import requests
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY = '32b0390040e3f3985e8e4dccffd92e11'

CITY = 'Bengaluru'

URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data from the API
response = requests.get(URL)
data = response.json()

# Extract temperature and timestamp
dates = []
temps = []

for entry in data['list']:
    dt = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
    temp = entry['main']['temp']
    dates.append(dt)
    temps.append(temp)

# Plot the temperature forecast
plt.figure(figsize=(10, 5))
plt.plot(dates, temps, marker='o', linestyle='-', color='blue')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
