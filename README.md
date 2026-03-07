
# WeatherDash – Command Line Weather Application

WeatherDash is a **Python command-line weather dashboard** that allows users to check current weather conditions and a **5-day forecast** for any city.

The application also allows users to **save favorite cities**, **switch temperature units**, and **view weather for multiple cities at once**.

WeatherDash uses the **Open-Meteo API** and follows a **modular Python project structure** using classes, functions, and multiple source files.

---

## Features

* Check **current weather conditions** for any city
* View a **5-day weather forecast**
* Display **weather emojis and ASCII weather icons**
* **Save favorite cities**
* **Remove cities from favorites**
* View **weather for all favorite cities**
* Switch **temperature units (Celsius / Fahrenheit)**
* Basic **weather alerts for high rain probability**

---

## Project Structure

```
weather-dashboard/
│
├── main.py                # CLI interface and menu system
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── src/
│   ├── __init__.py        # Makes src a Python package
│   ├── api.py             # Handles API requests
│   ├── utils.py           # Helper functions (emoji, ASCII art, conversions)
│   └── dashboard.py       # Main WeatherDashboard class
│
└── data/
    └── favorite_cities.json   # Stores saved favorite cities
```

---

## Technologies Used

* **Python 3**
* **Requests library**
* **Open-Meteo Weather API**
* **JSON file handling**
* **Command Line Interface (CLI)**

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## Usage

Run the application with:

```
python main.py
```

You will see the CLI menu:

```
====== WEATHER DASHBOARD ======

1. Check Weather
2. Add Favorite City
3. Show Favorite Cities
4. Remove Favorite City
5. Change Temperature Unit
6. Show Weather for Favorite Cities
7. Exit
```

Follow the prompts to interact with the dashboard.

---

## Example Output

```
☀️ WEATHER FOR KATIMA MULILO, NAMIBIA
=======================================================

Temperature : 18.2°C
Humidity    : 60%
Wind Speed  : 12 km/h

5-DAY FORECAST
---------------------------------------------
2026-03-07 ☀️ 14-19°C 10%
2026-03-08 ⛅ 13-18°C 20%
2026-03-09 🌧️ 12-17°C 60%
```

---

## Future Improvements

Possible improvements for future versions:

* Add **city search suggestions**
* Display **hourly weather forecasts**
* Add **colored CLI output**

---

## Author

Freeman
