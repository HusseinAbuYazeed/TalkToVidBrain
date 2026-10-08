import os
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

audio_file_path = Path("downloads/...")

with open(audio_file_path, "rb") as file:
    transcription = client.audio.transcriptions.create(
        file=file, 
        model="whisper-large-v3-turbo",
        response_format="text",
    )

print("transcript: ")
print(transcription)