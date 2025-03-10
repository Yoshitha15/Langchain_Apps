from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("The environment variable OPENAI_API_KEY is not set.")

os.environ["OPENAI_API_KEY"] = api_key
