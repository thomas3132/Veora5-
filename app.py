from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    
    # Call to the custom API
    response = requests.post('https://your-custom-api.com/generate', json={'prompt': prompt})
    
    if response.status_code == 200:
        image_url = response.json().get('image_url')
        return jsonify({'image_url': image_url}), 200
    else:
        return jsonify({'error': 'Image generation failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
