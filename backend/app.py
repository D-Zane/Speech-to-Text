from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import subprocess

app = Flask(__name__, template_folder='../frontend/templates')
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

#DEEPSPEECH_PATH = r'C:\Program Files\DeepSpeech\deepspeech.exe'  # Путь к DeepSpeech

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            print('No file part')
            return redirect(url_for('index'))
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(url_for('index'))
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Обработка файла с помощью DeepSpeech
            deepspeech_cmd = [
                'deepspeech',
                '--model', './DeepSpeech-2/deepspeech-0.9.3-models.pbmm',
                '--scorer', './DeepSpeech-2/deepspeech-0.9.3-models.scorer',
                '--audio', filepath
            ]
            result = subprocess.run(deepspeech_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if result.returncode != 0:
                print(f"DeepSpeech error: {result.stderr.decode('utf-8')}")
                return redirect(url_for('index'))
                
            transcription = result.stdout.decode('utf-8')
            return render_template('result.html', transcription=transcription, audio_file=file.filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)