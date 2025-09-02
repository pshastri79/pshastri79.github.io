import os
import openai
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display

              
api_key = OPENAI_API_KEY
# Add your openai_api_key above
if api_key: 
    print("Success!")
else:
    print("Failure")
openai = OpenAI()
message = "Hello, GPT! This is my first ever message to you! Hi!"
response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
print(response.choices[0].message.content)

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

ed = Website("https://priyashastri.wixsite.com/priyas")
print(ed.title)
print(ed.text)
