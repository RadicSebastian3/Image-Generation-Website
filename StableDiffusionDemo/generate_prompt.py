import requests
import random

API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}

default_prompt = 'Here is an example of a creative and long AI image generation prompt: Generate an image of '

def get_start_prompt():
    def get_random_word(file_path):
        with open(file_path, 'r') as file:
            nouns = file.read().splitlines()
        random_noun = random.choice(nouns)
        return random_noun

    random_noun = get_random_word('nouns.txt')
    random_adjective = get_random_word('adjectives.txt')

    generated_text = default_prompt + f'a{"n" if random_noun[0] in "aoeui" else ""} {random_noun} with a{"n" if random_adjective[0] in "aoeui" else ""} {random_adjective}'
    
    return {'full_prompt':generated_text, 'prompt':generated_text[len(default_prompt):], 'finished':False}

def get_random_prompt(current_prompt):
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    def generate_text(prompt):
        output = query({
            "inputs": prompt,
        })
        try:
            return output[0]['generated_text']
        except KeyError:
            raise Exception(output['error'])

    try:
        generated_text = generate_text(current_prompt)
    except Exception as e:
        return {'full_prompt':current_prompt, 'prompt':current_prompt[len(default_prompt)], 'finished':True, 'error':str(e)}

    finished = '.' in generated_text
    generated_text = generated_text.replace('.', '')

    prompt = generated_text[len(default_prompt):]

    if finished and len(prompt.split(' ')) <= 6:
        generated_text += f' and a '
        finished = False

    return {'full_prompt':generated_text, 'prompt':prompt, 'finished':finished, 'error':None}