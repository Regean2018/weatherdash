import requests  # Library used to send HTTP requests to APIs


# Get latitude and longitude of a city using the Open-Meteo geocoding API
def get_coordinates(city):

    # API endpoint for city geocoding
    url = "https://geocoding-api.open-meteo.com/v1/search"

    try:
        # Send request with city name and limit result to 1 match
        response = requests.get(
            url,
            params={"name": city, "count": 1},
            timeout=10  # Stop request if it takes longer than 10 seconds
        )

        # Convert API response to Python dictionary
        data = response.json()

        # Check if the API returned results
        if "results" in data and data["results"]:

            # Take the first location result
            loc = data["results"][0]

            # Return latitude, longitude, city name, and country
            return (
                loc["latitude"],
                loc["longitude"],
                loc["name"],
                loc.get("country", "")  # Use empty string if country not found
            )

    # Handle network or request errors
    except requests.RequestException:
        print("⚠ Network error")

    # Return None if no location was found
    return None


# Get weather data for given latitude and longitude
def get_weather(lat, lon):

    # Open-Meteo weather forecast API endpoint
    url = "https://api.open-meteo.com/v1/forecast"

    # Parameters specifying what weather data to retrieve
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max,weather_code",
        "timezone": "auto"
    }

    try:
        # Send request to the weather API
        response = requests.get(url, params=params, timeout=10)

        # Return the weather data as JSON
        return response.json()

    # Handle request errors
    except requests.RequestException:
        print("⚠ Could not fetch weather")
        return None