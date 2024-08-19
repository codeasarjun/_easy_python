from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# access environment variables
database_host = os.getenv('DATABASE_HOST')
database_port = os.getenv('DATABASE_PORT')

print(f"Database Host: {database_host}")
print(f"Database Port: {database_port}")
