# Task 1: Identifying and Creating Classes

class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city

    def fetch_weather_data(self):
        print(f"Fetching weather data for {self.city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(self.city, {})

class DataParser:
    def __init__(self, data):
        self.data = data

    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
    
class UserInterface(WeatherDataFetcher, DataParser):
    def __init__(self, city):
        super().__init__(city)

    def get_detailed_forecast(self):
        data = self.fetch_weather_data()
        return self.parse_weather_data(data)

    def display_weather(self):
        data = self.fetch_weather_data()
        if not data:
            print(f"Weather data not available for {self.city}")
        else:
            weather_report = self.parse_weather_data(data)
            print(weather_report)

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        user_interface = UserInterface(city)
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = user_interface.get_detailed_forecast()
        else:
            forecast = user_interface.display_weather()
        print(forecast)

if __name__ == "__main__":
    main()