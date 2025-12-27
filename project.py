import requests
import sys
from datetime import datetime, timezone, timedelta
def main():
    api = "d38fb5da72d8e5d0de61aac2a416350d"
    city = input("Enter Location: ").strip().lower()
    try:
        lat, lon = get_coordinates(city, api)
        weather_data = get_weather(lat, lon, api)
        print(format_output(weather_data, city))

    except ValueError as e:
        sys.exit(e)

def get_coordinates(city, api):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Error connecting to API")

    data = response.json()
    if not data:
        raise ValueError("City not found")
    return data[0]["lat"], data[0]["lon"]


def get_weather(lat, lon, api):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Error connecting to API")

    return response.json()

def calc_local_time(timezone_offset):
    utc_now = datetime.now(timezone.utc)
    delta = timedelta(seconds=timezone_offset)
    local_time = utc_now + delta

    return local_time.strftime("%Y-%m-%d %H:%M")


def get_emoji(description):
    description = description.lower()
    if "cloud" in description:
        return "☁️"
    elif "snow" in description:
        return "❄️"
    elif "rain" in description:
        return "🌧️"
    elif "fog" in description or "haze" in description:
        return "🌫️"
    elif "wind" in description:
        return "🍃"
    elif "clear" in description:
        return "☀️"
    else:
        return "🏙️"

def format_output(data, city):
    temprature = round(data["main"]["temp"])
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    timezone_offset = data["timezone"]
    local_time_s = calc_local_time(timezone_offset)
    desc_emoji = get_emoji(description)

    return f"Weather in {city.capitalize()}:\n🕒 Local Time: {local_time_s}\n🌡️  {temprature}°C\n{desc_emoji}  {description.capitalize()}\n💧 Humidity: {humidity}%"


if __name__ == "__main__":
    main()

