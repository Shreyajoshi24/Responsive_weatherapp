# Weather App Launcher
Write-Host "Starting Weather App..." -ForegroundColor Green
Write-Host ""
Write-Host "Make sure you have:" -ForegroundColor Yellow
Write-Host "1. Installed required packages: pip install flask requests python-dotenv" -ForegroundColor White
Write-Host "2. Set your OpenWeatherMap API key in main.py" -ForegroundColor White
Write-Host ""
Write-Host "The app will start on http://localhost:5000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Red
Write-Host ""

# Check if Python is installed
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "Python found. Starting application..." -ForegroundColor Green
    python main.py
} else {
    Write-Host "Python not found. Please install Python first." -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
