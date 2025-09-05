import os
import openai
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display

              
api_key = OPENAI_API_KEY
if api_key: 
    print("Success!")
else:
    print("Failure")
openai = OpenAI()

system_message = "You are an assistant that is great at KQL query generation"
user_prompt = "Give a KQL query to read 100 records the from azdailyamortizedconsumption table."
prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
  ]

response = openai.chat.completions.create(model="gpt-4o-mini", messages=prompts)
print(response.choices[0].message.content)
