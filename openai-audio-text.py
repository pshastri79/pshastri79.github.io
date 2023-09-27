# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
openai.organization = "org-jDhRxh2NbGke5U3xiiu823zz"
openai.api_key = os.getenv("OPEN_API_KEY")

audio_file= open("/Users/priyashastri/Desktop/2023-09-26 13.55.26 Priya Shastri's Personal Meeting Room/audio1643575195.m4a", "rb")
file_name_text = "2023-09-2613.55.26.txt"
transcript = openai.Audio.transcribe("whisper-1", audio_file)
f = open(file_name_text, "w+")
print(transcript, file=f)

f.close()
