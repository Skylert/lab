import requests
from datetime import datetime, timedelta

# This is to give a general idea on how to use python to retrieve data via API.  I am having
# issues setting up the correct parameters for what the tutorial was trying to teach.  Perhaps
# the video is old and the API has changed

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Get Paris weather for past week
#url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
#url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35"
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()
data.keys()
print(data)