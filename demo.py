# import requests
# import argparse
# from datetime import datetime
# import math
# # from tabulate import tabulate
# from rich import print
# from rich.table import Table
# from rich.console import Console
# from rich.text import Text
# import emoji

# API_KEY = "bb98bf2f8428ad68257a92b595bfd52e"


# def get_result(city):
#     CITY = city

#     url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         return data
#     except requests.exceptions.RequestException as e:
#         print(f"[bold red]Error fetching weather data for {city}: {e}[/bold red]")
#         return None
#     except ValueError as e:
#         print(f"[bold red]Error parsing weather data for {city}: {e}[/bold red]")
#         return None


# def calculate_dew_point(temperature, humidity):
#     # formula to calculate dew point
#     a = 17.27
#     b = 237.7
#     c = ((a * temperature) / (b + temperature)) + \
#         math.log(humidity / 100.0)
#     dew_point = (b * c) / (a - c)
#     return dew_point


# def calculate_feels_like_temperature(temperature, wind_speed):
#     # Formula to calculate feels like temperature (wind chill)
#     feels_like = 13.12 + 0.6215 * temperature - 11.37 * wind_speed**0.16 + 0.3965 * temperature * wind_speed**0.16
#     return feels_like



# def display_basic_weather(city, data):
#     temperature = data['main']['temp']
#     humidity = data['main']['humidity']
#     real_feel = calculate_feels_like_temperature(
#         temperature, data['wind']['speed'])

#     table = Table(show_header=True, header_style="bold magenta")
#     table.add_column("Location", style="dim")
#     table.add_column("Temperature (°C)", style="bold")
#     table.add_column("Humidity (%)", style="bold")
#     table.add_column("Real Feel (°C)", style="bold")

#     table.add_row(city, f"{temperature}°C", f"{humidity}%", f"{real_feel}°C")

#     console = Console()
#     console.print(f"Weather Information for {city}:", style="bold cyan")
#     console.print(table)
#     console.print()


# def display_additional_weather(data):
#     min_temp = data['main']['temp_min']
#     max_temp = data['main']['temp_max']
#     pressure = data['main']['pressure']
#     visibility = data['visibility']
#     wind_speed = data['wind']['speed']
#     uv_index = data.get('uvi', 'N/A')
#     sunrise_time = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
#     sunset_time = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
#     dew_point = calculate_dew_point(data['main']['temp'], data['main']['humidity'])

#     table = Table(show_header=True, header_style="bold magenta")
#     table.add_column("Parameter", style="dim")
#     table.add_column("Value", style="bold")

#     table.add_row("Minimum Temperature", f"{min_temp}°C")
#     table.add_row("Maximum Temperature", f"{max_temp}°C")
#     table.add_row("Pressure", f"{pressure} hPa")
#     table.add_row("Dew Point", f"{dew_point}°C")
#     table.add_row("Visibility", f"{visibility} meters")
#     table.add_row("Wind Speed", f"{wind_speed} m/s")
#     table.add_row("UV Index", f"{uv_index}")
#     table.add_row("Sunrise Time", sunrise_time)
#     table.add_row("Sunset Time", sunset_time)

#     console = Console()
#     console.print(table)
#     console.print()


# def generate_funny_tip(condition):
#     if "rain" in condition.lower():
#         return emoji.emojize("The sky is about to cry. Better grab your umbrella and some tissues! :umbrella_with_rain_drops:")
#     elif "cloud" in condition.lower():
#         return emoji.emojize("Cloudy skies ahead. Don't forget your jacket! :cloud:")
#     elif "sunny" in condition.lower():
#         return emoji.emojize("It's sunny outside. Don't forget your sunscreen! :sun_with_face:")
#     else:
#         return "No funny tip available for this weather condition."


# def calculate_temperature_difference(user_temp, typed_temp):
#     diff = user_temp - typed_temp
#     return f"Temperature difference: {abs(diff)}°C {'higher' if diff > 0 else 'lower'} than your location."


# def calculate_time_remaining(sunset_time):
#     now = datetime.now()
#     time_remaining = sunset_time - now
#     return f"Time remaining until sunset: {time_remaining}"


# def calculate_time_after_sunrise(sunrise_time):
#     now = datetime.now()
#     time_after_sunrise = now - sunrise_time
#     return f"Time after sunrise: {time_after_sunrise}"


# def main():
#     parser = argparse.ArgumentParser(
#         description='Get the current weather for a city')
#     parser.add_argument('cities', metavar='city', nargs='+',
#                         help='City name(s) for weather forecast')
#     parser.add_argument('-f', '--forecast', action='store_true',
#                         help='Display weather forecast for multiple days')

#     args = parser.parse_args()
#     cities = args.cities
#     user_location_temp = get_result("Puri")['main']['temp']

#     if args.forecast:
#         for city in cities:
#             forecast_data = get_forecast(city)
#             if forecast_data:
#                 print("Weather forecast for", city + ":")
#                 display_forecast(city, forecast_data)
#                 print()
#     else:
#         for city in cities:
#             weather_data = get_result(city)

#             if weather_data:
#                 display_basic_weather(city, weather_data)
#                 display_additional_weather(weather_data)

#                 temp_difference = calculate_temperature_difference(
#                     user_location_temp, weather_data['main']['temp'])
#                 print(temp_difference)

#                 funny_tip = generate_funny_tip(
#                     weather_data['weather'][0]['description'])
#                 print(funny_tip)

#                 sunset_time = datetime.fromtimestamp(
#                     weather_data['sys']['sunset'])
#                 print(calculate_time_remaining(sunset_time))

#                 sunrise_time = datetime.fromtimestamp(
#                     weather_data['sys']['sunrise'])
#                 print(calculate_time_after_sunrise(sunrise_time))

#             else:
#                 print()


# if __name__ == '__main__':
#     main()



import requests
import argparse
from datetime import datetime
import math
from rich import print
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
# import emoji

API_KEY = "bb98bf2f8428ad68257a92b595bfd52e"


def get_result(city):
    CITY = city

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"[bold red]Error fetching weather data for {city}: {e}[/bold red]")
        return None
    except ValueError as e:
        print(f"[bold red]Error parsing weather data for {city}: {e}[/bold red]")
        return None


def calculate_dew_point(temperature, humidity):
    # formula to calculate dew point
    a = 17.27
    b = 237.7
    c = ((a * temperature) / (b + temperature)) + \
        math.log(humidity / 100.0)
    dew_point = (b * c) / (a - c)
    return dew_point


def calculate_feels_like_temperature(temperature, wind_speed):
    # Formula to calculate feels like temperature (wind chill)
    feels_like = 13.12 + 0.6215 * temperature - 11.37 * wind_speed**0.16 + 0.3965 * temperature * wind_speed**0.16
    return feels_like


def display_weather(city, data):
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    real_feel = calculate_feels_like_temperature(
        temperature, data['wind']['speed'])
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    pressure = data['main']['pressure']
    visibility = data['visibility']
    wind_speed = data['wind']['speed']
    uv_index = data.get('uvi', 'N/A')
    sunrise_time = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
    sunset_time = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
    dew_point = calculate_dew_point(data['main']['temp'], data['main']['humidity'])

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Location", style="dim")
    table.add_column("Temperature (°C)", style="bold")
    table.add_column("Humidity (%)", style="bold")
    table.add_column("Real Feel (°C)", style="bold")
    table.add_column("Minimum Temperature", style="dim")
    table.add_column("Maximum Temperature", style="dim")
    table.add_column("Pressure", style="dim")
    table.add_column("Dew Point", style="dim")
    table.add_column("Visibility", style="dim")
    table.add_column("Wind Speed", style="dim")
    table.add_column("UV Index", style="dim")
    table.add_column("Sunrise Time", style="dim")
    table.add_column("Sunset Time", style="dim")

    table.add_row(
        city,
        f"{temperature}°C",
        f"{humidity}%",
        f"{real_feel}°C",
        f"{min_temp}°C",
        f"{max_temp}°C",
        f"{pressure} hPa",
        f"{dew_point}°C",
        f"{visibility} meters",
        f"{wind_speed} m/s",
        uv_index,
        sunrise_time,
        sunset_time
    )

    console = Console()
    console.print(Panel.fit(table, title=f"Weather Information for {city}:", style="bold cyan"))


def generate_funny_tip(condition):
    if "rain" in condition.lower():
        return "The sky is about to cry. Better grab your umbrella and some tissues! ☂️🌧"
    elif "cloud" in condition.lower():
        return "Cloudy skies ahead. Don't forget your jacket and sunglasses! 😎"
    elif "clear" in condition.lower():
        return "It's sunny outside. Don't forget your sunscreen! 🌞"
    elif "snow" in condition.lower():
        return "Bundle up and stay warm! ❄️⛄️"
    else:
        return "No funny tip available for this weather condition."


def calculate_temperature_difference(user_temp, typed_temp):
    diff = user_temp - typed_temp
    return f"Temperature difference: {abs(diff)}°C {'higher' if diff > 0 else 'lower'} than your location."


def calculate_time_remaining(sunset_time):
    now = datetime.now()
    time_remaining = sunset_time - now
    return f"Time remaining until sunset: {time_remaining}"


def calculate_time_after_sunrise(sunrise_time):
    now = datetime.now()
    time_after_sunrise = now - sunrise_time
    return f"Time after sunrise: {time_after_sunrise}"


def main():
    parser = argparse.ArgumentParser(
        description='Get the current weather for a city')
    parser.add_argument('cities', metavar='city', nargs='+',
                        help='City name(s) for weather forecast')
    parser.add_argument('-f', '--forecast', action='store_true',
                        help='Display weather forecast for multiple days')

    args = parser.parse_args()
    cities = args.cities
    user_location_temp = get_result("Puri")['main']['temp']

    if args.forecast:
        for city in cities:
            forecast_data = get_forecast(city)
            if forecast_data:
                print("Weather forecast for", city + ":")
                display_forecast(city, forecast_data)
                print()
    else:
        for city in cities:
            weather_data = get_result(city)

            if weather_data:
                console = Console()

                display_weather(city, weather_data)

                temp_difference = calculate_temperature_difference(
                    user_location_temp, weather_data['main']['temp'])
                console.print(Panel(temp_difference, title="Temperature Difference:", style="bold blue"))

                funny_tip = generate_funny_tip(
                    weather_data['weather'][0]['description'])
                console.print(Panel(funny_tip, title="Funny Tip:", style="bold yellow"))

                sunset_time = datetime.fromtimestamp(
                    weather_data['sys']['sunset'])
                console.print(Panel(calculate_time_remaining(sunset_time), title="Time Remaining Until Sunset:", style="bold green"))

                sunrise_time = datetime.fromtimestamp(
                    weather_data['sys']['sunrise'])
                console.print(Panel(calculate_time_after_sunrise(sunrise_time), title="Time After Sunrise:", style="bold magenta"))

            else:
                print()


if __name__ == '__main__':
    main()












# import requests
# import argparse
# from datetime import datetime
# from datetime import timedelta
# import math
# from rich import print
# from rich.table import Table
# from rich.console import Console
# from rich.panel import Panel
# import emoji

# API_KEY = "bb98bf2f8428ad68257a92b595bfd52e"


# def get_result(city):
#     CITY = city

#     url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         return data
#     except requests.exceptions.RequestException as e:
#         print(f"[bold red]Error fetching weather data for {city}: {e}[/bold red]")
#         return None
#     except ValueError as e:
#         print(f"[bold red]Error parsing weather data for {city}: {e}[/bold red]")
#         return None


# def calculate_dew_point(temperature, humidity):
#     # formula to calculate dew point
#     a = 17.27
#     b = 237.7
#     c = ((a * temperature) / (b + temperature)) + \
#         math.log(humidity / 100.0)
#     dew_point = (b * c) / (a - c)
#     return dew_point


# def calculate_feels_like_temperature(temperature, wind_speed):
#     # Formula to calculate feels like temperature (wind chill)
#     feels_like = 13.12 + 0.6215 * temperature - 11.37 * wind_speed**0.16 + 0.3965 * temperature * wind_speed**0.16
#     return feels_like


# def display_basic_info(city, data):
#     temperature = data['main']['temp']
#     humidity = data['main']['humidity']
#     real_feel = calculate_feels_like_temperature(
#         temperature, data['wind']['speed'])

#     console = Console()

#     table = Table(show_header=False)
#     table.add_column(justify="right")
#     table.add_column(justify="left")
#     table.add_row("Temperature:", f"{temperature}°C")
#     table.add_row("Humidity:", f"{humidity}%")
#     table.add_row("Real Feel:", f"{real_feel}°C")

#     basic_info_panel = Panel(
#         table,
#         title="Basic Info:",
#         style="bold cyan"
#     )
#     console.print(basic_info_panel)


# def display_additional_info(city, data):
#     min_temp = data['main']['temp_min']
#     max_temp = data['main']['temp_max']
#     pressure = data['main']['pressure']
#     dew_point = calculate_dew_point(
#         data['main']['temp'], data['main']['humidity'])
#     visibility = data['visibility']
#     wind_speed = data['wind']['speed']
#     uv_index = data.get('uvi', 'N/A')
#     sunrise_time = datetime.fromtimestamp(
#         data['sys']['sunrise']).strftime('%H:%M:%S')
#     sunset_time = datetime.fromtimestamp(
#         data['sys']['sunset']).strftime('%H:%M:%S')

#     sunrise = datetime.strptime(sunrise_time, "%H:%M:%S")
#     sunset = datetime.strptime(sunset_time, "%H:%M:%S")
#     current_time = datetime.now()
#     time_until_sunset = sunset - current_time
#     time_since_sunrise = current_time - sunrise

#     console = Console()

#     table = Table(show_header=False)
#     table.add_column(justify="right")
#     table.add_column(justify="left")
#     table.add_row("Minimum Temperature:", f"{min_temp}°C")
#     table.add_row("Maximum Temperature:", f"{max_temp}°C")
#     table.add_row("Pressure:", f"{pressure} hPa")
#     table.add_row("Dew Point:", f"{dew_point}°C")
#     table.add_row("Visibility:", f"{visibility} meters")
#     table.add_row("Wind Speed:", f"{wind_speed} m/s")
#     table.add_row("UV Index:", uv_index)
#     table.add_row("Sunrise Time:", sunrise_time)
#     table.add_row("Sunset Time:", sunset_time)
#     table.add_row("Time Until Sunset:", str(time_until_sunset).split('.')[0])
#     table.add_row("Time Since Sunrise:", str(time_since_sunrise).split('.')[0])

#     additional_info_panel = Panel(
#         table,
#         title="Additional Info:",
#         style="bold cyan"
#     )
#     console.print(additional_info_panel)


# def generate_funny_tip(condition):
#     if "rain" in condition.lower():
#         return "The sky is about to cry. Better grab your umbrella and some tissues! ☂️🌧"
#     elif "cloud" in condition.lower():
#         return "Cloudy skies ahead. Don't forget your jacket and sunglasses! 😎"
#     elif "clear" in condition.lower():
#         return "It's sunny outside. Don't forget your sunscreen! 🌞"
#     elif "snow" in condition.lower():
#         return "Bundle up and stay warm! ❄️⛄️"
#     else:
#         return "No funny tip available for this weather condition."


# def display_weather_info(city, data):
#     condition = data['weather'][0]['description']

#     console = Console()

#     weather_info_panel = Panel(
#         f"Weather Information for {city}:\n\nCondition: {condition.title()}",
#         title="",
#         style="bold white",
#         width=100
#     )
#     console.print(weather_info_panel)

#     display_basic_info(city, data)
#     display_additional_info(city, data)

#     funny_tip = generate_funny_tip(condition)
#     if funny_tip:
#         funny_tip_panel = Panel(funny_tip, title="Funny Tip:", style="bold magenta")
#         console.print(funny_tip_panel)


# def main():
#     parser = argparse.ArgumentParser(description="Weather App")
#     parser.add_argument("city", type=str, help="City name")
#     args = parser.parse_args()

#     city = args.city

#     data = get_result(city)
#     if data:
#         display_weather_info(city, data)


# if __name__ == "__main__":
#     main()
