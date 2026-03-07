# Return an emoji and description based on the weather code
def weather_emoji(code):

    # Dictionary mapping weather codes to emoji and text description
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

    # Return matching emoji and description, or default if code not found
    return emojis.get(code, ("🌡️", "Unknown"))


# Convert temperature from Celsius to the selected unit
def convert_temp(celsius, unit):

    # Convert to Fahrenheit if requested
    if unit == "fahrenheit":
        return (celsius * 9 / 5) + 32, "°F"

    # Otherwise return Celsius
    return celsius, "°C"


# Display simple ASCII art based on the weather code
def ascii_weather(code):

    # Sunny weather
    if code == 0:

        print("""
     \\   /
      .-.
   ― (   ) ―
      `-’
     /   \\
     SUNNY
""")

    # Cloudy weather
    elif code in [1, 2, 3]:

        print("""
      .--.
   .-(    ).
  (___.__)__)
     CLOUDY
""")

    # Rainy weather
    elif code in [51, 61, 63, 80]:

        print("""
      .--.
   .-(    ).
  (___.__)__)
   ‘ ‘ ‘ ‘
      RAIN
""")

    # Thunderstorm weather
    elif code == 95:

        print("""
      .--.
   .-(    ).
  (___.__)__)
      ⚡⚡⚡
   THUNDER
""")