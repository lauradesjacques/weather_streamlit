# IMPORTS
import streamlit as st
import folium
from utils import *
import os
import requests
from dotenv import load_dotenv
import folium
from streamlit_folium import folium_static


# st.set_page_config(layout="wide")
# st.title('weather forecast by city')
# st.map()

# COORDONEES PARIS latitude=48.866667, longitude=2.333333

# ==================================================================================>
def fetch_data_city_locality(city):
    load_dotenv('.env')
    key=os.environ['KEY']
    URL = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        longitude = data[0]["lat"]
        latitude  = data[0]["lon"] 
        return longitude, latitude
    else:
        return st.error("ERROR !")
# ==================================================================================>
def fetch_data_city(latitude, longitude):
    load_dotenv('.env')
    key=os.environ['KEY']
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}"
    response = requests.get(URL) 
    if response.status_code == 200:
        data = response.json()
        data = {
            "wind"          :data["wind"],
            "weather"       :data["weather"],
            "humidity"      :data["main"]["humidity"],
            "pressure"      :data['main']["pressure"],
            "visibility"    :data["visibility"],
            "sunrise"       :data["sys"]["sunrise"],
            "sunset"        :data["sys"]["sunset"],
        }
        return data
    else:
        return st.error("ERROR !")
# ==================================================================================>
def map_city(latitude, longitude, city):
    st.header("City Location on Map 🗺️")
    map_center = [latitude, longitude]
    m = folium.Map(location=map_center, zoom_start=10)
    folium.Marker(map_center, popup=city.capitalize()).add_to(m)
    folium_static(m) 
# ==================================================================================>
def main():
    background_front(url="https://medias.objectifgard.com/api/v1/images/view/6363e8dcb8e2787e72787ae6/article/image.jpg")
    # INPUT CITY.
    name_of_city = st.text_input("Rechercher une ville...")
    
    if not name_of_city == "":
        
        try:
            # Récupérationn de la localisation de la ville choisis.
            longitude, latitude = fetch_data_city_locality(city=name_of_city)

            # Récupération de la météo de la ville choisis.
            data = fetch_data_city(latitude, longitude)
            
            # Style CSS.
            st.markdown("""
            <style>
                .card {
                    border: 2px solid #e2e8f0;
                    border-radius: 0.5rem;
                    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
                    padding: 1rem;
                    margin: 1rem;
                }
                .header {
                    text-align: center;
                    font-size: 1.5rem;
                    font-weight: bold;
                    margin-bottom: 1rem;
            </style>
            """, unsafe_allow_html=True)

            # # CARD_1_WEATHER
            st.markdown(
            f'''<div class="card">
                <div class="header">Météo de {name_of_city}</div>
                <p>Longitude   : {longitude}          </p>
                <p>Latitude    : {latitude}           </p>
                <p>Humidity    : {data["humidity"]}   </p>
                <p>Visibility  : {data["visibility"]} </p>
                <p>Sunrise     : {data["sunrise"]}    </p>
                <p>Sunset      : {data["sunset"]}     </p>
            </div>''', 
            unsafe_allow_html=True
            )
            
            # Affichage de la map
            map_city(latitude=longitude, longitude=latitude, city=name_of_city)
            
        except:
            st.error("Ville introuvable ou inexistante")
            

main()








# CARD_2_PREDICTION
# st.markdown('<div class="card"><div class="header">Forecast 8 days</div><p>Day 1 </p><p>Day2</p> <p>Day3</p><p>Day4</p></div>', unsafe_allow_html=True)
# <p>Weather     : {data["weather"]}        </p>
# <p>Wind        : {data["wind"]}           </p> 