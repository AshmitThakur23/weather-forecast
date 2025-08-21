from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your OpenWeatherMap API key!
API_KEY = "5ff7bbb8eaadffe49d08ece4f5644a7b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required."})

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "Could not fetch weather data."})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

