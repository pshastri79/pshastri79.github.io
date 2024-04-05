import openai
import os
import requests
import bs4


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"

#SPAIN
#FRANCE
country_newspapers = {"Spain":("https://www.elpais.com", ".c_t"), 
                      "France":("https://www.lemonde.fr", ".article__title-label")}


tag = "article__title-label"

def create_prompt():
    country = input("what country are you interested to read news?")
    try:
        url,tag = country_newspapers[country]
    except:
        print("Sorry country not supported")
        return
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    country_headlines=[]
    for item in soup.select('.article__title'):
        country_headlines += item.getText()+ '\n'
    prompt = "Detect the language in the news headline below, then translate the summary of headline to English"
    return prompt+"".join(country_headlines)

prompt = create_prompt()
print(prompt)

response = openai.Completion.create(model="gpt-3.5-turbo-instruct", 
                                    prompt=prompt, 
                                    temperature=0.1, 
                                    max_tokens=300, 
                                    top_p=1.0)
print(response['choices'][0]['text'])