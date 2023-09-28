# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
import re
openai.organization = "org-jDhRxh2NbGke5U3xiiu823zz"
openai.api_key = os.getenv("OPEN_API_KEY")

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
filepath = "/Users/priyashastri/Desktop/2023-09-26 13.55.26 Priya Shastri's Personal Meeting Room/audio1643575195.m4a"
audio_file= open("/Users/priyashastri/Desktop/2023-09-26 13.55.26 Priya Shastri's Personal Meeting Room/audio1643575195.m4a", "rb")
file_name_text=filepath.split(" ")
file_name_str = []
for item in file_name_text:
    if item[0] in nums:
        file_name_str.append(item.strip())
    elif item[-1] in nums:
        i = 0
        while i < len(item):
            if item[-1-i] in nums or item[-1-i] == '-':
               i += 1
            else:
                break
        file_name_str.append(item[-i:])  
            
print(file_name_str)
file_name_str.append(".txt")
file_name_str = "".join(file_name_str)
print(file_name_str)

transcript = openai.Audio.transcribe("whisper-1", audio_file)
f = open(file_name_str, "w+")
print(transcript, file=f)

f.close()

