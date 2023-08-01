from weather_analysis import *

ip_address = get_ip_address()
current_city = get_current_city(ip_address)
weather_data = weather_data(current_city)

temp_cel = str(weather_data['temp_c']) + "°" + " C"
temp_fer = str(weather_data['temp_f']) + "°" + " F"
weather_condition = weather_data['condition']
humidity = weather_data['humidity']


