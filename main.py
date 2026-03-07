"""
WeatherDash - Command Line Weather Application

Author: Regean Pitiya
Uses Open-Meteo API to display current weather and forecasts.
"""

# Import the main WeatherDashboard class
from src.dashboard import WeatherDashboard


# Main function that runs the CLI weather dashboard
def main():

    # Create the weather dashboard application
    app = WeatherDashboard()

    # Run the program continuously until the user exits
    while True:

        # Display menu options
        print("\n====== WEATHER DASHBOARD ======\n")

        print("1. Check Weather")
        print("2. Add Favorite City")
        print("3. Show Favorite Cities")
        print("4. Remove Favorite City")
        print("5. Change Temperature Unit")
        print("6. Show Weather for Favorite Cities")
        print("7. Exit")

        # Get user's menu selection
        choice = input("Select option: ")

        # Option 1: Show weather for a city
        if choice == "1":

            city = input("Enter city: ")
            app.display_weather(city)

        # Option 2: Add a city to favorites
        elif choice == "2":

            city = input("City to add: ")
            app.add_favorite(city)

        # Option 3: Display saved favorite cities
        elif choice == "3":

            app.show_favorites()
        
        # Option 4: Remove a city from favorites
        elif choice == "4":

            app.remove_favorite()

        # Option 5: Change temperature unit
        elif choice == "5":

            app.change_unit()

        # Option 6: Show weather for all favorite cities
        elif choice == "6":
            app.show_favorites_weather()

        # Option 7: Exit the application
        elif choice == "7":

            print("Goodbye!")
            break

        # Handle invalid menu input
        else:

            print("Invalid option")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()