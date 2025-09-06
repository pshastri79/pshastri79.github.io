import os
import openai
from openai import OpenAI
import requests
from IPython.display import Markdown, display
import gradio as gr

              
api_key = OPENAI_API_KEY
if api_key: 
    print("Success!")
else:
    print("Failure")
openai = OpenAI()
    
MODEL = "gpt-4o-mini"

system_message = "You are an assistant that is great KQL query generation"
user_prompt = "Give a KQL query to read 100 records the from azdailyamortizedconsumption table."
prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
  ]

response = openai.chat.completions.create(model=MODEL, messages=prompts)
print(response.choices[0].message.content)

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(fn=chat, type="messages").launch()
