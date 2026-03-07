import json  # Used to read/write favorite cities from a JSON file
from src.api import get_coordinates, get_weather  # Functions for location and weather API calls
from src.utils import weather_emoji, convert_temp, ascii_weather  # Helper display functions


# Class that manages the weather dashboard features
class WeatherDashboard:

    def __init__(self):

        # File where favorite cities are stored
        self.favorites_file = "data/favorite_cities.json"

        # Load saved favorite cities when the app starts
        self.favorites = self.load_favorites()

        # Default temperature unit
        self.unit = "celsius"

    # Load favorite cities from JSON file
    def load_favorites(self):

        try:
            # Open and read the favorites file
            with open(self.favorites_file, "r") as f:
                return json.load(f)

        # If file doesn't exist or is invalid, return empty list
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # Save current favorites list to the JSON file
    def save_favorites(self):

        with open(self.favorites_file, "w") as f:
            json.dump(self.favorites, f, indent=2)

    # Show a warning if rain probability is high
    def weather_alert(self, rain):

        if rain >= 70:
            print("⚠ Weather Alert: Heavy rain expected!")

        elif rain >= 40:
            print("☔ Possible rain today")

    # Display weather information for a given city
    def display_weather(self, city):

        # Get latitude and longitude of the city
        coords = get_coordinates(city)

        # If city is not found, stop the function
        if not coords:
            print("❌ City not found")
            return

        # Unpack returned coordinates and location info
        lat, lon, name, country = coords

        # Request weather data from the API
        weather = get_weather(lat, lon)

        # Stop if weather data could not be retrieved
        if not weather:
            return

        # Extract current weather and forecast data
        current = weather["current"]
        daily = weather["daily"]

        # Convert temperature to selected unit
        temp, unit = convert_temp(current["temperature_2m"], self.unit)

        # Get weather emoji and description
        emoji, desc = weather_emoji(current["weather_code"])

        # Print header for weather display
        print("\n" + "=" * 55)
        print(f"{emoji} WEATHER FOR {name.upper()}, {country.upper()}")
        print("=" * 55)

        # Display ASCII weather art
        ascii_weather(current["weather_code"])

        # Show current weather details
        print(f"""
{emoji} {desc}

Temperature : {temp:.1f}{unit}
Humidity    : {current['relative_humidity_2m']}%
Wind Speed  : {current['wind_speed_10m']} km/h
""")

        print("5-DAY FORECAST")
        print("-" * 45)

        # Loop through forecast days (maximum 5)
        for i in range(min(5, len(daily["time"]))):

            # Date of the forecast
            date = daily["time"][i]

            # Convert daily max and min temperatures
            max_t, _ = convert_temp(daily["temperature_2m_max"][i], self.unit)
            min_t, _ = convert_temp(daily["temperature_2m_min"][i], self.unit)

            # Rain probability for that day
            rain = daily["precipitation_probability_max"][i]

            # Get emoji for forecast weather
            emoji, _ = weather_emoji(daily["weather_code"][i])

            # Print forecast line
            print(f"{date} {emoji} {min_t:.0f}-{max_t:.0f}{unit}  {rain}%")

            # Check if rain alert should be shown
            self.weather_alert(rain)

    # Add a city to the favorites list
    def add_favorite(self, city):

        # Verify city by getting coordinates
        coords = get_coordinates(city)

        if not coords:
            print("❌ City not found")
            return

        # Extract city name and country
        _, _, name, country = coords

        full_name = f"{name}, {country}"

        # Add city only if it is not already saved
        if full_name not in self.favorites:

            self.favorites.append(full_name)

            # Save updated favorites list
            self.save_favorites()

            print(f"⭐ Added {full_name}")

        else:
            print("City already saved")

    # Display list of saved favorite cities
    def show_favorites(self):

        if not self.favorites:
            print("📭 No favorites saved")
            return

        print("\n⭐ Favorite Cities")

        # Show numbered list of cities
        for i, city in enumerate(self.favorites, 1):
            print(f"{i}. {city}")

    # Switch temperature unit between Celsius and Fahrenheit
    def change_unit(self):

        if self.unit == "celsius":
            self.unit = "fahrenheit"
        else:
            self.unit = "celsius"

        print(f"Temperature unit set to {self.unit}")

    # Display weather for all favorite cities
    def show_favorites_weather(self):

        if not self.favorites:
            print("📭 No favorite cities saved")
            return

        print("\n⭐ WEATHER FOR FAVORITE CITIES\n")

        # Loop through each favorite city
        for city in self.favorites:
            print("-" * 55)
            self.display_weather(city)

    # Remove a city from favorites
    def remove_favorite(self):

        if not self.favorites:
            print("📭 No favorite cities saved")
            return

        print("\n⭐ Favorite Cities")

        # Show numbered list of favorites
        for i, city in enumerate(self.favorites, 1):
            print(f"{i}. {city}")

        # Ask user which city to remove
        choice = input("Enter number of city to remove: ")

        # Check if the input is a number
        if choice.isdigit():

            index = int(choice) - 1

            # Ensure number corresponds to a valid city
            if 0 <= index < len(self.favorites):

                # Remove the selected city
                removed = self.favorites.pop(index)

                # Update the favorites file
                self.save_favorites()

                print(f"❌ Removed {removed}")

            else:
                print("Invalid number")

        else:
            print("Invalid input")