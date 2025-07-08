// DOM Elements
const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchBtn');
const loading = document.getElementById('loading');
const weatherCard = document.getElementById('weatherCard');
const errorMessage = document.getElementById('errorMessage');

// Weather data elements
const cityName = document.getElementById('cityName');
const country = document.getElementById('country');
const temperature = document.getElementById('temperature');
const feelsLike = document.getElementById('feelsLike');
const description = document.getElementById('description');
const weatherIcon = document.getElementById('weatherIcon');
const humidity = document.getElementById('humidity');
const pressure = document.getElementById('pressure');
const windSpeed = document.getElementById('windSpeed');
const visibility = document.getElementById('visibility');
const timestamp = document.getElementById('timestamp');
const errorText = document.getElementById('errorText');

// Event Listeners
searchBtn.addEventListener('click', handleSearch);
cityInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        handleSearch();
    }
});

// Auto-focus on input when page loads
window.addEventListener('load', function() {
    cityInput.focus();
});

// Handle search functionality
async function handleSearch() {
    const city = cityInput.value.trim();
    
    if (!city) {
        showError('Please enter a city name');
        return;
    }
    
    await getWeatherData(city);
}

// Fetch weather data from the backend
async function getWeatherData(city) {
    showLoading();
    hideError();
    hideWeatherCard();
    
    try {
        const response = await fetch('/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ city: city })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch weather data');
        }
        
        displayWeatherData(data);
        
    } catch (error) {
        console.error('Error fetching weather data:', error);
        showError(error.message || 'Failed to fetch weather data. Please try again.');
    } finally {
        hideLoading();
    }
}

// Display weather data on the UI
function displayWeatherData(data) {
    // Update text content
    cityName.textContent = data.city;
    country.textContent = data.country;
    temperature.textContent = data.temperature;
    feelsLike.textContent = data.feels_like;
    description.textContent = data.description;
    humidity.textContent = `${data.humidity}%`;
    pressure.textContent = `${data.pressure} hPa`;
    windSpeed.textContent = `${data.wind_speed} m/s`;
    visibility.textContent = `${data.visibility} km`;
    timestamp.textContent = data.timestamp;
    
    // Update weather icon
    const iconUrl = `https://openweathermap.org/img/wn/${data.icon}@2x.png`;
    weatherIcon.src = iconUrl;
    weatherIcon.alt = data.description;
    
    // Show weather card
    showWeatherCard();
}

// UI Helper Functions
function showLoading() {
    loading.style.display = 'block';
}

function hideLoading() {
    loading.style.display = 'none';
}

function showWeatherCard() {
    weatherCard.style.display = 'block';
}

function hideWeatherCard() {
    weatherCard.style.display = 'none';
}

function showError(message) {
    errorText.textContent = message;
    errorMessage.style.display = 'block';
    
    // Auto-hide error after 5 seconds
    setTimeout(() => {
        hideError();
    }, 5000);
}

function hideError() {
    errorMessage.style.display = 'none';
}

// Additional Features

// Clear input on focus (optional)
cityInput.addEventListener('focus', function() {
    this.select();
});

// Detect user's location and get weather (optional feature)
function getUserLocationWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            async function(position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                
                try {
                    // You can extend the backend to handle coordinates
                    // For now, we'll use a reverse geocoding service or default city
                    await getWeatherData('Current Location');
                } catch (error) {
                    console.error('Error getting location weather:', error);
                }
            },
            function(error) {
                console.error('Geolocation error:', error);
            }
        );
    }
}

// Add a button for current location (you can add this to HTML if needed)
function addLocationButton() {
    const locationBtn = document.createElement('button');
    locationBtn.innerHTML = '<i class="fas fa-location-arrow"></i>';
    locationBtn.className = 'location-btn';
    locationBtn.title = 'Get weather for current location';
    locationBtn.onclick = getUserLocationWeather;
    
    // You can append this to the search container if needed
    // document.querySelector('.search-container').appendChild(locationBtn);
}

// Handle API key warning
function checkAPIKey() {
    fetch('/health')
        .then(response => response.json())
        .then(data => {
            console.log('Backend health check:', data);
        })
        .catch(error => {
            console.error('Backend health check failed:', error);
            showError('Backend server is not responding. Please check your setup.');
        });
}

// Check backend health on page load
window.addEventListener('load', function() {
    setTimeout(checkAPIKey, 1000);
});

// Add some sample cities for quick testing (optional)
const sampleCities = ['London', 'New York', 'Tokyo', 'Paris', 'Sydney'];

// You can add a suggestions feature
function addCitySuggestions() {
    const suggestionContainer = document.createElement('div');
    suggestionContainer.className = 'city-suggestions';
    
    sampleCities.forEach(city => {
        const suggestion = document.createElement('button');
        suggestion.textContent = city;
        suggestion.className = 'suggestion-btn';
        suggestion.onclick = () => {
            cityInput.value = city;
            handleSearch();
        };
        suggestionContainer.appendChild(suggestion);
    });
    
    // You can append this to the search container if needed
    // document.querySelector('.search-container').after(suggestionContainer);
}

// Error handling for network issues
window.addEventListener('online', function() {
    hideError();
});

window.addEventListener('offline', function() {
    showError('You are offline. Please check your internet connection.');
});
