from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file:
        file_details = {
            "filename": file.filename,
            "content_type": file.content_type,
            "content_length": file.content_length
        }
        return jsonify(file_details)
    else:
        return jsonify({"error": "Invalid file"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
