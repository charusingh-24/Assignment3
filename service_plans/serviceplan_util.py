from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from typing import Optional
import random
import string

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a dictionary to store the API request limits for each user

api_limits = {
    "free": {
        "limit": 10,
        "reset_interval": "1 hour"
    },
    "Gold": {
        "limit": 15,
        "reset_interval": "1 hour"
    },
    "Platinum": {
        "limit": 20,
        "reset_interval": "1 hour"
    }
}


def generate_api_key(length=16):
    """Generate a random API key."""
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))


# Define a decorator function to check the API request limits for each user
def check_api_limits(api_key: str):
    # Get the current time
    now = datetime.utcnow()

    # Check if the user is in the api_limits dictionary
    if api_key in api_limits:
        # Check if the user has exceeded their API request limit
        if api_limits[api_key]['count'] >= api_limits[api_key]['limit']:
            # Check if the reset time has already passed
            if now < api_limits[api_key]['reset_time']:
                # Raise an exception if the user has exceeded their API request limit
                raise HTTPException(status_code=429, detail="API request limit exceeded. Please try again later.")
            else:
                # Reset the user's API request limit if the reset time has passed
                api_limits[api_key]['count'] = 1
                api_limits[api_key]['reset_time'] = now + timedelta(hours=1)
        else:
            # Increment the user's API request count if they have not exceeded their limit
            api_limits[api_key]['count'] += 1
    else:
        # Add the user to the api_limits dictionary if they are not already in it
        api_limits[api_key] = {'count': 1, 'limit': 10, 'reset_time': now + timedelta(hours=1)}


