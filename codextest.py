import openai
import os
import inspect
from pathlib import Path

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"

# Python
# Function (OOP)

def hello(name):
    print(f"Hello {name}")
    

    
def docstring_prompt(code):
    prompt = f"{code}\n # A high quality python doc string of the above function.:\n  \"\"\""
    return(prompt)



def merge_docstring_and_function(orig_function, docstring):
    function_string = inspect.getsource(orig_function)
    split_parts = function_string.split("\n")
    first_part = split_parts[0]
    second_part = split_parts[1:]
    
    prompt = docstring_prompt(function_string)

    
    response = openai.Completion.create(model="gpt-3.5-turbo-instruct", 
                                    prompt=prompt, 
                                    temperature = 0, 
                                    max_tokens=100, 
                                    top_p=1.0, 
                                    stop=["\"\"\""])
    docstring = response['choices'][0]['text']
    output_function = "".join(first_part)+ "\n" + "\"\"\"\n" +docstring+"\"\"\"\n"+ "\n".join(second_part) 
    
    print(output_function)
    
def hello_v2(name, pet):
    print(f"Hello {name}\n")
    print(f"feed {pet}\n")
    print("All done\n")
    

    

merge_docstring_and_function(hello_v2, " ")    