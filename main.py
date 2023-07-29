from weather_analysis import *
# import streamlit as st

ip_address = get_ip_address()
current_city = get_current_city(ip_address)
weather_data = weather_data(current_city)

temp_cel = str(weather_data['temp_c']) + "°" + " C"
temp_fer = str(weather_data['temp_f']) + "°" + " F"
weather_condition = weather_data['condition']
humidity = weather_data['humidity']
# print(weather_data)

# print(f"------------------- Your Current Weather Condition --------------------")
# print(f"IP ADDRESS: {ip_address}")
# print(f"CURRENT CITY: {current_city}")
# print(f"CURRENT TEMPERATURE (C): {weather_data['temp_c']}")
# print(f"CLOUD: {weather_data['condition']}")
# print(f"HUMIDITY: {weather_data['humidity']}")

# ## Giving some trial of streamlit pyhton module
#
# unit = 'cel'
# st.write(f"CITY: {current_city}")
# # unit_button = st.button(unit)
# # print(unit_button)
# if st.button("cel"):
#     st.button("Fer")
#     st.write(f"temperature: {weather_data['temp_c']}")
# else:
#     st.write(f"temperature: {weather_data['temp_f']}")


# =================================================================== #


