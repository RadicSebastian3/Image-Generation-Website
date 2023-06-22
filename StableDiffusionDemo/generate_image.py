import requests
from PIL import Image
from io import BytesIO

ngrok_url = 'https://49f1-2001-871-23c-590a-92b7-7f20-7268-63f5.ngrok-free.app'  

def get_generated_image(prompt):
    print(f"Generating \"{prompt}\"...")
    response = requests.post(f'{ngrok_url}/generate_image', data={'text_prompt': prompt})
    image = Image.open(BytesIO(response.content))
    print("Image successfully generated\n")
    return image

while False:
    prompt = input("Enter the text prompt: ")
    print(f"Generating \"{prompt}\"... (~30 seconds)")
    generated_image = get_generated_image(prompt)
    generated_image.show()
    generated_image.save(f'{prompt}.png')
    print(f"Successfully generated {prompt}.png\n")
