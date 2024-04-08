import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"

prompt = "What does the kubernetes engine do and does it have a company?"

response = openai.Completion.create(model="gpt-3.5-turbo-instruct", 
                                    prompt=prompt, 
                                    temperature=0.1, 
                                    max_tokens=300, 
                                    top_p=1.0)
print(response['choices'][0]['text'])

