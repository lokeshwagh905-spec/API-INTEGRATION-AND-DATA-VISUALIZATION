import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# OpenWeatherMap API Key
# -----------------------------------
API_KEY = "b15bb38ee9e04e8b794cd2baec8c5bbd"

# -----------------------------------
# Cities for Weather Analysis
# -----------------------------------
cities = ["Delhi", "Mumbai", "Pune", "Indore", "Bhopal"]

# -----------------------------------
# Lists to Store Data
# -----------------------------------
city_names = []
temperatures = []
humidity_levels = []
weather_conditions = []

# -----------------------------------
# Fetch Weather Data from API
# -----------------------------------
for city in cities:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()
    
    print(data)

    # Extract Data
    city_names.append(city)
    temperatures.append(data['main']['temp'])
    humidity_levels.append(data['main']['humidity'])
    weather_conditions.append(data['weather'][0]['main'])

# -----------------------------------
# Create DataFrame
# -----------------------------------
df = pd.DataFrame({
    'City': city_names,
    'Temperature': temperatures,
    'Humidity': humidity_levels,
    'Condition': weather_conditions
})

# -----------------------------------
# Print Data
# -----------------------------------
print("\nWeather Data:\n")
print(df)

# -----------------------------------
# Create Visualization Dashboard
# -----------------------------------
plt.figure(figsize=(12, 5))

# -----------------------------------
# Temperature Bar Chart
# -----------------------------------
plt.subplot(1, 2, 1)

sns.barplot(
    x='City',
    y='Temperature',
    data=df
)

plt.title("Temperature Comparison")
plt.ylabel("Temperature (°C)")

# -----------------------------------
# Humidity Line Chart
# -----------------------------------
plt.subplot(1, 2, 2)

sns.lineplot(
    x='City',
    y='Humidity',
    data=df,
    marker='o'
)

plt.title("Humidity Levels")
plt.ylabel("Humidity (%)")

# -----------------------------------
# Adjust Layout
# -----------------------------------
plt.tight_layout()

# -----------------------------------
# Save Dashboard Image
# -----------------------------------
plt.savefig("weather_dashboard.png")

# -----------------------------------
# Show Dashboard
# -----------------------------------
plt.show()
