import requests
import os

def get_weather(city_name, api_key):
    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Complete URL with city name and API key
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    # Send GET request to the URL
    response = requests.get(complete_url)
    
    # Convert response to JSON format
    weather_data = response.json()
    
    # Check if the city is found
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        wind = weather_data["wind"]
        weather = weather_data["weather"][0]
        
        # Extract the required information
        temperature = main["temp"]
        apparent_temperature = main["feels_like"]
        wind_speed = wind["speed"] * 3.6  # Convert from m/s to km/h
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_type = weather["description"]
        
        # Create the output string
        output = (
            f"City: {city_name}\n"
            f"Temperature: {temperature} °C\n"
            f"Apparent Temperature: {apparent_temperature} °C\n"
            f"Wind Speed: {wind_speed} km/h\n"
            f"Air Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Weather: {weather_type.capitalize()}\n"
        )
        
        # Print the weather information
        print(output)
        
        # Ask the user if they want to save the output
        save_option = input("Do you want to save the output to a file? (yes/no): ").strip().lower()
        
        if save_option == 'yes' or 'Yes' or 'y' or 'Y':
            # Get the desktop path
            desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            
            # Get the filename from the user
            file_name = input("Enter the filename (with .txt extension): ").strip()
            file_path = os.path.join(desktop_path, file_name)
            
            # Write the output to the file
            with open(file_path, 'w') as file:
                file.write(output)
            print(f"Output saved to Desktop")
    else:
        print("City Not Found")

if __name__ == "__main__":
    # Input the city name
    city_name = input("Enter city name: ")
    
    # Your OpenWeatherMap API key
    api_key = input("Enter API key: ")
    
    # Call the function to get weather
    get_weather(city_name, api_key)
