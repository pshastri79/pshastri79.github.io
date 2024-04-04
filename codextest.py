import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"

# Python
# Function (OOP)

def hello(name):
    print(f"Hello {name}")
    

    
def docstring_prompt(code):
    prompt = f"{code}\n # A high quality python doc string of the above function.:\n  \"\"\""
    return(prompt)

import inspect
prompt = docstring_prompt(inspect.getsource(hello))

    
response = openai.Completion.create(model="gpt-3.5-turbo-instruct", 
                                    prompt=prompt, 
                                    temperature = 0, 
                                    max_tokens=100, 
                                    top_p=1.0, 
                                    stop=["\"\"\""])
print(response['choices'][0]['text'])

