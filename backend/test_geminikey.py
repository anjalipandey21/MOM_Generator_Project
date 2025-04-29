from dotenv import load_dotenv
import os

load_dotenv()  # This loads the .env file
print("Gemini Key:", os.getenv("GEMINI_API_KEY"))
