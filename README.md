# Speech-to-Text

Для установки DeepSpeech-2 скачайте репозиторий:

```bash
    https://github.com/cogmeta/DeepSpeech-2.git
```
Для корректной работы DeepSpeech нужно установить обученные модели:

```bash
    curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
    curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```
Как только все будет установлено, вы сможете использовать двоичный файл deepspeech для преобразования речи в текст в коротких, примерно 5-секундных аудиофайлах (в настоящее время в клиенте Python поддерживаются только файлы WAV с 16-битным разрешением, 16 кГц, mono).:

```bash
    pip3 install deepspeech
```
