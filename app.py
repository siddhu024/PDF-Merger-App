from flask import Flask, render_template, request, send_file
import os
from merger import merge_pdfs

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FILE = "merged.pdf"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    files = request.files.getlist('pdfs')
    file_paths = []

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        file_paths.append(path)

    merge_pdfs(file_paths, OUTPUT_FILE)

    return send_file(OUTPUT_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)