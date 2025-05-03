import requests

def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city
    }
    try:
        response = requests.get(base_url, params=params)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return None

def main():
    api_key = "Insert key here"  # Replace with your WeatherAPI.com API key
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Description: {weather_data['current']['condition']['text']}")
    else:
        print("Failed to fetch weather data. Please check the city name and try again.")

if __name__ == "__main__":
    main() 
