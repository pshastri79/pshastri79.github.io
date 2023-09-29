import os
import openai
import datetime
openai.organization = "org-jDhRxh2NbGke5U3xiiu823zz"
openai.api_key = os.getenv("OPEN_API_KEY")
# Example OpenAI Python library request

MODEL = "gpt-3.5-turbo"
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Together We grow: explain"},
    ],
    temperature=0,
)

print(response['choices'][0]['message']['content'])
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
lines_str = response['choices'][0]['message']['content'].split(".")
for line in lines_str:
    f.write(line)
f.close()
