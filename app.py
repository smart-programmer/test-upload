from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file:
        # Get image details
        image = Image.open(file)
        image_format = image.format
        image_size = image.size
        image_mode = image.mode

        # Convert image to base64
        image_bytes = BytesIO()
        image.save(image_bytes, format=image_format)
        image_base64 = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

        file_details = {
            "filename": file.filename,
            "content_type": file.content_type,
            "content_length": file.content_length,
            "image_format": image_format,
            "image_size": image_size,
            "image_mode": image_mode,
            "image_base64": image_base64
        }

        return jsonify(file_details)
    else:
        return jsonify({"error": "Invalid file"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
