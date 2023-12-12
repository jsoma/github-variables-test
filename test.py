import os
from dotenv import load_dotenv
load_dotenv()
PROJECT_API_KEY = os.getenv('PROJECT_API_KEY')
PROJECT_API_KEY_SECRET = os.getenv('PROJECT_API_KEY_SECRET')

print("Here goes")
print(PROJECT_API_KEY)
print(PROJECT_API_KEY_SECRET)
