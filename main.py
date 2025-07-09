from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = "4d45ad92f0f807afc8066920ea7f96cb"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"  # Note: using http instead of https

def get_weather_data(city):
    """
    Fetch weather data from OpenWeatherMap API
    """
    try:
        # Parameters for the API request
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # For Celsius temperature
        }
        
        # Make API request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()


#this is some change that I want to be in this proj
        
        # Extract relevant weather information
        weather_info = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'].title(),
            'icon': data['weather'][0]['icon'],
            'wind_speed': data['wind']['speed'],
            'visibility': data.get('visibility', 0) / 1000,  # Convert to km
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        # Handle specific HTTP errors
        if hasattr(e, 'response') and e.response is not None:
            if e.response.status_code == 401:
                return {'error': 'Invalid API key. Please check your OpenWeatherMap API key and ensure it is activated.'}
            elif e.response.status_code == 404:
                return {'error': 'City not found. Please check the spelling and try again.'}
            elif e.response.status_code == 429:
                return {'error': 'API rate limit exceeded. Please try again later.'}
            else:
                return {'error': f'API request failed with status {e.response.status_code}: {str(e)}'}
        return {'error': f'API request failed: {str(e)}'}
    except KeyError as e:
        return {'error': f'Invalid response format: {str(e)}'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}

@app.route('/')
def index():
    """
    Render the main page
    """
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    """
    API endpoint to get weather data
    """
    try:
        data = request.get_json()
        city = data.get('city', '').strip()
        
        if not city:
            return jsonify({'error': 'City name is required'}), 400
        
        weather_data = get_weather_data(city)
        
        if 'error' in weather_data:
            return jsonify(weather_data), 400
        
        return jsonify(weather_data)
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/health')
def health_check():
    """
    Health check endpoint
    """
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    # Check if API key is set
    if API_KEY == "your_api_key_here":
        print("Warning: Please set your OpenWeatherMap API key in main.py")
        print("You can get a free API key from: https://openweathermap.org/api")
    else:
        print(f"Using API key: {API_KEY[:8]}...")
        print("Testing API key...")
        
        # Test API key with a simple request
        test_result = get_weather_data("London")
        if 'error' in test_result:
            print(f"⚠️  API Key Test Failed: {test_result['error']}")
            print("\nPossible solutions:")
            print("1. Check if your API key is correct")
            print("2. Wait up to 2 hours for new API keys to activate")
            print("3. Verify your API key at: https://home.openweathermap.org/api_keys")
            print("4. Make sure you haven't exceeded your usage limits")
        else:
            print("✅ API Key Test Successful!")
            print(f"Test result: {test_result['city']}, {test_result['temperature']}°C")
    
    print(f"\nStarting server on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
