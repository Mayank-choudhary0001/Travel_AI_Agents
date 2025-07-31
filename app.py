
from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

user_preferences = {
    "destination": "Goa",
    "travel_dates": {"start": "2025-12-01", "end": "2025-12-07"},
    "interests": ["beaches", "local cuisine", "adventure sports"],
    "budget": 20000
}

@app.route('/')
def home():
    return "Travel Planner Agent is running."

@app.route('/weather')
def get_weather():
    city = request.args.get('city', default='Goa')
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/itinerary', methods=['GET'])
def generate_itinerary():
    destination = user_preferences['destination']
    interests = ", ".join(user_preferences['interests'])
    itinerary = {
        "day_1": f"Arrival in {destination}, check-in, beach exploration.",
        "day_2": f"Local cuisine tour and water sports.",
        "day_3": f"Adventure sports and local market visit.",
        "day_4": f"Sunset cruise and cultural evening.",
        "day_5": f"Free day for exploration and leisure.",
        "day_6": f"Local sightseeing and souvenir shopping.",
        "day_7": f"Check-out and return travel."
    }
    return jsonify({"destination": destination, "interests": interests, "itinerary": itinerary})

@app.route('/map')
def get_map():
    origin = request.args.get('origin', default='Mumbai')
    destination = request.args.get('destination', default='Goa')
    maps_url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}"
    return jsonify({"map_link": maps_url})

if __name__ == '__main__':
    app.run(debug=True)
