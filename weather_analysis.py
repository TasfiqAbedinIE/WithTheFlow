import forecast_weather as fw
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity


def get_ip_address():
    """
    Function gets global IP address from the computer
    :return:
    """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        data = response.json()
        global_ip = data["ip"]
        return global_ip

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


# ip_address = get_ip_address()
# print(ip_address)


def get_current_city(ip_address):
    """
    Function gets current city, region and country based on the ip_address
    :param ip_address:
    :return:
    """
    res = DbIpCity.get(str(ip_address), api_key="free")
    current_city = res.city
    current_region = res.region
    current_country = res.country
    return current_city


# current_city = get_current_city(ip_address)
# print(current_city)


## variable to get current weather update using forecast_weather module


def weather_data(current_city):
    """
    Function te get current weather condition based on the real time city
    :param current_city:
    :return:
    """
    status = fw.get_current(location=current_city)
    forecast = fw.get_forecast(location=current_city, days="3")

    # print(status)
    # print(forecast)
    return status


# weather_data(current_city)


