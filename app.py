# IMPORTS
import streamlit as st
import folium

st.set_page_config(layout="wide")
st.title('weather forecast by city')
st.map()

# COORDONEES PARIS latitude=48.866667, longitude=2.333333

# INPUT CITY
name_of_city = st.text_input(' ', 'Enter city name')


# Style CSS
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


# CARD_1_WEATHER
st.markdown('<div class="card"><div class="header">Weather</div><p>Temperature</p><p>Wind</p> <p>Humidity</p><p>Visibility</p></div>', unsafe_allow_html=True)

# CARD_2_PREDICTION
st.markdown('<div class="card"><div class="header">Forecast 8 days</div><p>Day 1 </p><p>Day2</p> <p>Day3</p><p>Day4</p></div>', unsafe_allow_html=True)
