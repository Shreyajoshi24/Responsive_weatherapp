#!/usr/bin/env python3
"""
OpenWeatherMap API Key Tester
This script helps you test your API key and diagnose issues.
"""

import requests
import json
from datetime import datetime

# Your API key
API_KEY = "4d45ad92f0f807afc8066920ea7f96cb"

def test_api_key():
    """Test the API key with different endpoints and methods"""
    
    print("🌤️  OpenWeatherMap API Key Tester")
    print("=" * 50)
    print(f"API Key: {API_KEY[:8]}...{API_KEY[-4:]}")
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test different endpoints
    test_cases = [
        {
            "name": "Current Weather (HTTP)",
            "url": f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"
        },
        {
            "name": "Current Weather (HTTPS)", 
            "url": f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"
        },
        {
            "name": "API Key Validation",
            "url": f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['name']}")
        print("-" * 30)
        
        try:
            response = requests.get(test_case['url'], timeout=10)
            
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print("✅ SUCCESS!")
                print(f"City: {data.get('name', 'N/A')}")
                print(f"Temperature: {data.get('main', {}).get('temp', 'N/A')}°")
                print(f"Description: {data.get('weather', [{}])[0].get('description', 'N/A')}")
                
            elif response.status_code == 401:
                print("❌ UNAUTHORIZED (401)")
                error_data = response.json()
                print(f"Error: {error_data.get('message', 'Invalid API key')}")
                print("\n🔧 Solutions:")
                print("   • Check if your API key is correct")
                print("   • Wait up to 2 hours for new keys to activate")
                print("   • Verify at: https://home.openweathermap.org/api_keys")
                
            elif response.status_code == 404:
                print("❌ NOT FOUND (404)")
                print("City not found or API endpoint issue")
                
            elif response.status_code == 429:
                print("❌ RATE LIMIT EXCEEDED (429)")
                print("Too many requests. Wait and try again.")
                
            else:
                print(f"❌ ERROR ({response.status_code})")
                try:
                    error_data = response.json()
                    print(f"Message: {error_data.get('message', 'Unknown error')}")
                except:
                    print(f"Response: {response.text[:200]}")
                    
        except requests.exceptions.Timeout:
            print("❌ TIMEOUT - Request took too long")
            
        except requests.exceptions.ConnectionError:
            print("❌ CONNECTION ERROR - Check your internet connection")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ REQUEST ERROR: {str(e)}")
            
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {str(e)}")
            
        print()
    
    # Additional diagnostics
    print("📋 Additional Information:")
    print("-" * 30)
    print("• Free tier allows 1,000 calls/day")
    print("• New API keys can take up to 2 hours to activate")
    print("• Check your usage at: https://home.openweathermap.org/statistics")
    print("• Documentation: https://openweathermap.org/api")

if __name__ == "__main__":
    test_api_key()
