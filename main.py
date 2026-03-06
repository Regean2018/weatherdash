# Weather Dashboard
# Features:
# - Current weather
# - 5-day forecast
# - Save favorite cities
# - Weather alerts
# - Temperature conversion (C/F)
# - ASCII weather art

import requests
import json


class WeatherDashboard:

    def __init__(self):
        # File where favorite cities are stored
        self.favorites_file = "favorite_cities.json"

        # Load saved cities
        self.favorites = self.load_favorites()

        # Default temperature unit
        self.unit = "celsius"

    # -----------------------------
    # Load favorite cities from file
    # -----------------------------
    def load_favorites(self):

        try:
            with open(self.favorites_file, "r") as f:
                return json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # -----------------------------
    # Save favorite cities to file
    # -----------------------------
    def save_favorites(self):

        with open(self.favorites_file, "w") as f:
            json.dump(self.favorites, f, indent=2)

    # -----------------------------
    # Get coordinates of city
    # -----------------------------
    def get_coordinates(self, city):

        url = "https://geocoding-api.open-meteo.com/v1/search"

        try:
            response = requests.get(
                url,
                params={"name": city, "count": 1},
                timeout=10
            )

            data = response.json()

            if "results" in data and data["results"]:

                loc = data["results"][0]

                return (
                    loc["latitude"],
                    loc["longitude"],
                    loc["name"],
                    loc.get("country", "")
                )

        except requests.RequestException:
            print("⚠ Network error")

        return None

    # -----------------------------
    # Get weather data
    # -----------------------------
    def get_weather(self, lat, lon):

        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max,weather_code",
            "timezone": "auto"
        }

        try:

            response = requests.get(url, params=params, timeout=10)

            return response.json()

        except requests.RequestException:

            print("⚠ Could not fetch weather")

            return None

    # -----------------------------
    # Weather emoji + description
    # -----------------------------
    def weather_emoji(self, code):

        emojis = {

            0: ("☀️", "Clear sky"),
            1: ("🌤️", "Mainly clear"),
            2: ("⛅", "Partly cloudy"),
            3: ("☁️", "Overcast"),
            45: ("🌫️", "Fog"),
            48: ("🌫️", "Fog"),
            51: ("🌧️", "Light drizzle"),
            61: ("🌧️", "Rain"),
            63: ("🌧️", "Rain"),
            71: ("🌨️", "Snow"),
            80: ("🌧️", "Rain showers"),
            95: ("⛈️", "Thunderstorm")

        }

        return emojis.get(code, ("🌡️", "Unknown"))

    # -----------------------------
    # Temperature conversion
    # -----------------------------
    def convert_temp(self, celsius):

        if self.unit == "fahrenheit":

            return (celsius * 9 / 5) + 32, "°F"

        return celsius, "°C"

    # -----------------------------
    # ASCII weather art
    # -----------------------------
    def ascii_weather(self, code):

        if code == 0:

            print("""
     \\   /
      .-.
   ― (   ) ―
      `-’
     /   \\
     SUNNY
""")

        elif code in [1, 2, 3]:

            print("""
      .--.
   .-(    ).
  (___.__)__)
     CLOUDY
""")

        elif code in [51, 61, 63, 80]:

            print("""
      .--.
   .-(    ).
  (___.__)__)
   ‘ ‘ ‘ ‘
      RAIN
""")

        elif code == 95:

            print("""
      .--.
   .-(    ).
  (___.__)__)
      ⚡⚡⚡
   THUNDER
""")

    # -----------------------------
    # Weather alerts
    # -----------------------------
    def weather_alert(self, rain):

        if rain >= 70:

            print("⚠ Weather Alert: Heavy rain expected!")

        elif rain >= 40:

            print("☔ Possible rain today")

    # -----------------------------
    # Display weather
    # -----------------------------
    def display_weather(self, city):

        coords = self.get_coordinates(city)

        if not coords:

            print("❌ City not found")

            return

        lat, lon, name, country = coords

        weather = self.get_weather(lat, lon)

        if not weather:

            return

        current = weather["current"]

        daily = weather["daily"]

        temp, unit = self.convert_temp(current["temperature_2m"])

        emoji, desc = self.weather_emoji(current["weather_code"])

        print("\n" + "=" * 55)

        print(f"  {emoji} WEATHER FOR {name.upper()}, {country.upper()}")

        print("=" * 55)

        self.ascii_weather(current["weather_code"])

        print(f"""
  {emoji} {desc}

  🌡 Temperature : {temp:.1f}{unit}
  💧 Humidity    : {current['relative_humidity_2m']}%
  💨 Wind Speed  : {current['wind_speed_10m']} km/h
""")

        print("📅 5-DAY FORECAST")

        print("-" * 45)

        for i in range(min(5, len(daily["time"]))):

            date = daily["time"][i]

            max_t, _ = self.convert_temp(daily["temperature_2m_max"][i])

            min_t, _ = self.convert_temp(daily["temperature_2m_min"][i])

            rain = daily["precipitation_probability_max"][i]

            emoji, _ = self.weather_emoji(daily["weather_code"][i])

            print(f"{date} {emoji} {min_t:.0f}-{max_t:.0f}{unit}  💧{rain}%")

            self.weather_alert(rain)

        print("=" * 55)

    # -----------------------------
    # Add favorite city
    # -----------------------------
    def add_favorite(self, city):

        coords = self.get_coordinates(city)

        if not coords:

            print("❌ City not found")

            return

        _, _, name, country = coords

        full_name = f"{name}, {country}"

        if full_name not in self.favorites:

            self.favorites.append(full_name)

            self.save_favorites()

            print(f"⭐ Added {full_name}")

        else:

            print("City already saved")

    # -----------------------------
    # Show favorite cities
    # -----------------------------
    def show_favorites(self):

        if not self.favorites:

            print("📭 No favorites saved")

            return

        print("\n⭐ Favorite Cities")

        for i, city in enumerate(self.favorites, 1):

            print(f"{i}. {city}")

    # -----------------------------
    # Change temperature unit
    # -----------------------------
    def change_unit(self):

        if self.unit == "celsius":

            self.unit = "fahrenheit"

        else:

            self.unit = "celsius"

        print(f"Temperature unit set to {self.unit}")


# -----------------------------
# Main Menu
# -----------------------------
def main():

    app = WeatherDashboard()

    while True:

        print("\n====== WEATHER DASHBOARD ======")

        print("1. Check Weather")

        print("2. Add Favorite City")

        print("3. Show Favorite Cities")

        print("4. Change Temperature Unit")

        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":

            city = input("Enter city: ")

            app.display_weather(city)

        elif choice == "2":

            city = input("City to add: ")

            app.add_favorite(city)

        elif choice == "3":

            app.show_favorites()

        elif choice == "4":

            app.change_unit()

        elif choice == "5":

            print("Goodbye!")

            break

        else:

            print("Invalid option")


# Run program
if __name__ == "__main__":

    main()