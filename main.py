from flask import Flask, request, send_file, render_template
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    file = request.files['image']
    quality = int(request.form.get('quality', 85))
    
    img = Image.open(file.stream)
    
    output = io.BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)
    output.seek(0)
    
    return send_file(output, mimetype='image/jpeg', as_download=True, download_name='compressed.jpg')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Vercel 需要这个
app.debug = False