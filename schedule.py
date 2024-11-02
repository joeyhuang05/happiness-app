import random
import time
from datetime import datetime, timedelta
import requests

def schedule_random_prompt():
    # Set a random time for the prompt (between 10 AM and 8 PM)
    random_hour = random.randint(10, 20)
    random_minute = random.randint(0, 59)
    
    now = datetime.now()
    target_time = now.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)
    
    # If the target time is already past, schedule for the next day
    if target_time <= now:
        target_time += timedelta(days=1)
    
    print(f"Scheduled prompt for: {target_time}")
    
    # Wait until the target time
    while datetime.now() < target_time:
        time.sleep(30)  # Sleep to avoid busy waiting
    
    # Send the prompt to the Flask app or trigger data collection
    response = requests.post('http://localhost:5000/get_happinese', json={'prompt': 'How happy are you today on a scale from 1 to 10?'})
    print("Prompt sent:", response.json())

if __name__ == "__main__":
    schedule_random_prompt()
