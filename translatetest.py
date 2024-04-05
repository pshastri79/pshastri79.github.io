import openai
import os
import requests
import bs4


country = input("what country are you interested to read news?")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"

#SPAIN
#FRANCE
country_newspapers = {"Spain":("https://www.elpais.com", ".c_t"), 
                      "France":("https://www.lemonde.fr", ".article__title-label")}

url = country_newspapers[country]
response = requests.get(url)
tag = "article__title-label"

soup = bs4.BeautifulSoup(response.text, "lxml")
print(soup.select('.article__title')[0].getText())
