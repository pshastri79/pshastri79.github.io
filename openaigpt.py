import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"


''' response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                        messages=[{"role":"system", "content":"You are a math teacher"}, 
                                                {"role":"user", "content":"what is Pythagoras theorem?"},
                                                {"role":"assistant", "content":"Pythagoras's theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. In mathematical terms,it can be expressed as:(c^2 = a^2 + b^2\)"},
                                                {"role":"user", "content":"Where is this theorem used?"}]
                                       )
print(response['choices'][0]['message']['content']) '''
class Createbot():
    def __init__(self, system_prompt):
        self.system = system_prompt
        self.messages=[{"role":"system", "content":system_prompt}]
    
    def chat(self):
        print("To termination conversation type 'END'") 
        question = " "
        
        user_str = []
        assistant_str = []
        while question!="END" or question !='end':
            question=input("")
            
            self.messages.append({'role':'user','content':question})
            print(self.messages)
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                                    messages=self.messages)
            
            content = response['choices'][0]['message']['content']
            print(content)
            self.messages.append({'role':'assistant','content':content})
            
system_prompt=input()
mathtutor = Createbot(system_prompt)
mathtutor.chat()

    
