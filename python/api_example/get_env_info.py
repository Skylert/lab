from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_URL")
debug = os.environ.get("DEBUG")

print(f"API Key: {api_key}")
print(f"Database: {database}")
print(f"Debug mode: {debug}")
