# Utility functions

import datetime
import requests
import json
import os

def get_current_time():
    """
    Returns the current date and time.
    
    Usage: What time is it, Get current date, Check current time
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city):
    """
    Gets the current weather for a specified city using a API.
    
    Usage: Check weather, Get temperature, Weather forecast
    
    Args:
        city (str): The name of the city
    """
    try:
        # Using a free weather API
        api_key = "api_key"  # In production, use environment variables
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return {
                "city": data["name"],
                "temperature": f"{data['main']['temp']}°C",
                "feels_like": f"{data['main']['feels_like']}°C",
                "description": data["weather"][0]["description"],
                "humidity": f"{data['main']['humidity']}%"
            }
        else:
            return f"Error: {data['message']}"
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

def create_reminder(message, time=None):
    """
    Creates a reminder with a message and optional time.
    
    Usage: Set reminder, Create alert, Remind me
    
    Args:
        message (str): The reminder message
        time (str, optional): Time for the reminder (format: "YYYY-MM-DD HH:MM:SS")
    """
    reminder = {
        "message": message,
        "time": time if time else get_current_time(),
        "created_at": get_current_time()
    }
    
    # In a real app, this would be stored in a database
    reminders_file = "reminders.json"
    try:
        if os.path.exists(reminders_file):
            with open(reminders_file, "r") as f:
                reminders = json.load(f)
        else:
            reminders = []
        
        reminders.append(reminder)
        
        with open(reminders_file, "w") as f:
            json.dump(reminders, f, indent=2)
            
        return f"Reminder set: {message}"
    except Exception as e:
        return f"Error setting reminder: {str(e)}"
