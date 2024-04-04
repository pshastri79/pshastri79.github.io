import os
import openai
import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization="org-jDhRxh2NbGke5U3xiiu823zz"

#client = OpenAI(api_key=os.getenv("OPEN_API_KEY"), organization="org-jDhRxh2NbGke5U3xiiu823zz")

# TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(organization="org-jDhRxh2NbGke5U3xiiu823zz")'
# openai.organization = "org-jDhRxh2NbGke5U3xiiu823zz"
# Example OpenAI Python library request

MODEL = "gpt-3.5-turbo"
response = client.chat.completions.create(model=MODEL,
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Knock knock."},
    {"role": "assistant", "content": "Who's there?"},
    {"role": "user", "content": "Explain seek your frequency"},
],
temperature=0)

print(response.choices[0].message.content)
def create_file_name_timestamp():
    filename_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(filename_str)
    filename_str_1 = []
    filename_str_1.append(filename_str)
    filename_str_1.append(".txt")
    return("".join(filename_str_1))

file_name_str = create_file_name_timestamp()
print(file_name_str)
f = open(file_name_str, "w+")
lines_str = response.choices[0].message.content.split(".")
for line in lines_str:
    f.write(line)
f.close()
