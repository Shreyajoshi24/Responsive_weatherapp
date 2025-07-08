@echo off
echo Starting Weather App...
echo.
echo Make sure you have:
echo 1. Installed required packages: pip install flask requests python-dotenv
echo 2. Set your OpenWeatherMap API key in main.py
echo.
echo The app will start on http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
pause
python main.py
