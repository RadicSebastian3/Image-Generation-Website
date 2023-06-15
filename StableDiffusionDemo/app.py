from flask import Flask, render_template, request, send_file, jsonify
import json
from io import BytesIO
from generate_image import get_generated_image
from generate_prompt import get_start_prompt, get_random_prompt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt', '')
    image = get_generated_image(prompt)
    
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

@app.route('/generate_random_prompt', methods=['GET'])
def generate_random_prompt():
    try:
        prompt = request.args.get('current_prompt')
        if prompt == '':
            return json.dumps(get_start_prompt())

        return json.dumps(get_random_prompt(prompt))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
