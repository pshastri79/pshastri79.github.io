import base64
import openai
import os
from PIL import Image
from io import BytesIO

def encode_image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffer = BytesIO()
        img.save(buffer, format="PNG")  # Use PNG format
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return img_str

# Example usage:
image_path = "/Users/priyashastri/Desktop/witlogoTC.png"
base64_image = encode_image_to_base64(image_path)

# Now, you can include the base64_image in your OpenAI API request
# as part of the content list with type "image_url"


# Replace with your API key and image path
openai.api_key = os.getenv("OPEN_API_KEY")


# Encode the image
# with open(image_path, "rb") as image_file:
#    image_data = base64.b64encode((image_file.read()).decode('utf-8'))


# Construct the request
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,[{base64_image}]",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

# Print the response
print(response.choices[0].message.content)
