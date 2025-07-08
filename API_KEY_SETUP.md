# 🔑 API Key Setup Guide

## Current Issue
❌ **401 Unauthorized Error**: Your current API key is invalid or not activated.

## Quick Fix Steps

### Step 1: Get Valid API Key
1. Visit: https://openweathermap.org/api
2. Sign up for FREE account (if you don't have one)
3. Go to "API Keys" section in your dashboard
4. Generate a new API key
5. **Wait up to 2 hours** for activation (important!)

### Step 2: Update Your Code
1. Open `main.py`
2. Find this line:
   ```python
   API_KEY = "YOUR_NEW_VALID_API_KEY_HERE"
   ```
3. Replace `YOUR_NEW_VALID_API_KEY_HERE` with your actual API key

### Step 3: Test Your API Key
Run the tester:
```bash
python test_api.py
```

### Step 4: Start Your App
```bash
python main.py
```

## Troubleshooting

### Common Issues:
- **New keys need 2 hours to activate** ⏰
- **Free tier: 1,000 calls/day limit** 📊
- **Check spelling of API key** 🔍

### Verify Your Key:
- Login to: https://home.openweathermap.org/api_keys
- Check if key shows as "Active"
- Verify usage statistics

## Need Help?
- OpenWeatherMap FAQ: https://openweathermap.org/faq#error401
- API Documentation: https://openweathermap.org/api

## Success! ✅
When working, you'll see:
- "✅ API Key Test Successful!" when starting the app
- Weather data displays correctly in browser
