import unittest
from io import BytesIO
import wave
from app import app
import os

class FlaskFileUploadTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Удалить все файлы из папки загрузки после каждого теста
        folder = app.config['UPLOAD_FOLDER']
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)

    def create_wav_file(self):
        buffer = BytesIO()
        with wave.open(buffer, 'wb') as wf:
            wf.setnchannels(1)  # mono
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(16000)  # 16 kHz
            wf.writeframes(b'\x00\x00' * 16000)  # 1 second of silence
        buffer.seek(0)
        return buffer

    def test_upload_file(self):
        wav_file = self.create_wav_file()
        data = {
            'file': (wav_file, 'test.wav')
        }
        response = self.app.post('/upload', content_type='multipart/form-data', data=data)

        # Проверка, что запрос успешен и был перенаправлен на результат
        self.assertEqual(response.status_code, 200)

        # Проверка, что файл действительно был сохранен
        self.assertTrue(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'test.wav')))

if __name__ == '__main__':
    unittest.main()
