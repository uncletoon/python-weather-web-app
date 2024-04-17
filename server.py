from flask import Flask, render_template, request
from werather import get_weather_current
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # CHeck for empty stings or strings with only spaces
    if not bool(city.strip()):
        city = "New York city"

    weather_data = get_weather_current(city)
    
    # If the city is not found By API.
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)