import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()    
        description = data["weather"][0]["description"]  
        temp_kelvin = data["main"]["temp"]  
        temp_celsius = temp_kelvin - 273.15
        return description, temp_celsius
    else:
        return None, None

if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"  
    city = input("Enter municipality name: ")
    description, temp_celsius = get_weather(city, api_key)
    if description is not None:
        print(f"Weather in {city}: {description}")
        print(f"Temperature: {temp_celsius:.2f} °C")
    else:
        print("Could not fetch weather data.")
