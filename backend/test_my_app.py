import unittest
import app 



class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_upload_file(self):
        # Сначала загружаем файл
        with open('./uploads/2830-3980-0043.wav', 'rb') as f:
            rv = self.app.post('/upload', data={'file': f})
        # Проверяем код ответа
        self.assertEqual(rv.status_code, 200)
        # Проверяем, что на странице результатов есть текст
        self.assertIn(b'Transcription Result', rv.data)

    def test_empty_upload(self):
        # Тест на загрузку пустого файла
        rv = self.app.post('/upload', data={'file': None})
        # Проверяем код ответа
        self.assertEqual(rv.status_code, 400)
        # Проверяем, что на странице ошибки есть текст
        self.assertIn(b'Error: No file provided', rv.data)

if __name__ == '__main__':
    unittest.main()
