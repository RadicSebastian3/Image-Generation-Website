from flask import Flask, render_template, request, send_file, jsonify
from io import BytesIO
from generate_image import get_generated_image

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

if __name__ == '__main__':
    app.run(debug=True)
