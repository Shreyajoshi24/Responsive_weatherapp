# Weather App

A modern, responsive weather application built with Python Flask backend and vanilla HTML/CSS/JavaScript frontend.

## Features

- 🌤️ Real-time weather data from OpenWeatherMap API
- 🎨 Beautiful and responsive UI design
- 📱 Mobile-friendly interface
- 🔍 Search weather by city name
- 📊 Detailed weather information including:
  - Temperature and "feels like" temperature
  - Humidity and pressure
  - Wind speed and visibility
  - Weather description and icons
  - Timestamp of last update

## Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key (free registration required)

## Setup Instructions

### 1. Get OpenWeatherMap API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to your account dashboard
4. Generate a new API key

### 2. Install Dependencies

```bash
pip install flask requests python-dotenv
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

1. Open `main.py`
2. Replace `"your_api_key_here"` with your actual OpenWeatherMap API key:

```python
API_KEY = "your_actual_api_key_here"
```

### 4. Run the Application

```bash
python main.py
```

The application will start on `http://localhost:5000`

## Project Structure

```
weather-app/
│
├── main.py                 # Flask backend application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── README.md              # Project documentation
│
├── templates/
│   └── index.html         # Main HTML template
│
└── static/
    ├── css/
    │   └── style.css      # Stylesheet
    └── js/
        └── script.js      # JavaScript functionality
```

## API Endpoints

- `GET /` - Main application page
- `POST /weather` - Get weather data for a city
- `GET /health` - Health check endpoint

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter a city name in the search box
3. Click the search button or press Enter
4. View the detailed weather information

## Features Explanation

### Backend (Python Flask)
- RESTful API design
- Error handling and validation
- OpenWeatherMap API integration
- JSON response formatting

### Frontend (HTML/CSS/JavaScript)
- Responsive design that works on all devices
- Modern UI with smooth animations
- Real-time weather data display
- Error handling and loading states
- Accessibility features

## Customization

### Styling
- Modify `static/css/style.css` to change colors, fonts, and layout
- The design uses CSS Grid and Flexbox for responsive layout
- Font Awesome icons for weather symbols

### Functionality
- Edit `static/js/script.js` to add new features
- Modify `main.py` to extend API functionality
- Add new weather data fields by updating both backend and frontend

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure you've replaced the placeholder API key with your actual key
2. **Module Not Found**: Install required packages using `pip install -r requirements.txt`
3. **Network Error**: Check your internet connection and API key validity
4. **City Not Found**: Ensure the city name is spelled correctly

### Debug Mode

The application runs in debug mode by default. To disable:

```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## Support

If you encounter any issues or have questions, please check the troubleshooting section or create an issue in the project repository.
