# Speech-to-Text

## Необходимые компоненты

* [Python 3.6](https://www.python.org/)
* Mac or Linux environment (Мы используем Anaconda) (https://www.anaconda.com/download)

## Установка необходимых библиотек

Воспользуемся requrements.txt для установки необходимых библиотек:

```bash
pip install -r requirements.txt
```

## Установка DeepSpeech-2

Для установки DeepSpeech-2 скачайте репозиторий:

```bash
git clone https://github.com/cogmeta/DeepSpeech-2.git
```

Для корректной работы DeepSpeech нужно установить предобученные модели:

```bash
cd DeppSpeech-2
```

```bash
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```

Загрузить примеры аудио файлов:

```bash
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/audio-0.9.3.tar.gz
tar xvf audio-0.9.3.tar.gz
```

Как только все будет установлено, вы сможете использовать двоичный файл deepspeech для преобразования речи в текст в коротких, примерно 5-секундных аудиофайлах (в настоящее время в клиенте Python поддерживаются только файлы WAV с 16-битным разрешением, 16 кГц, mono).:

```bash
pip3 install deepspeech
```
## Запуск Веб-Интерфейса

Запуск происходит при помощи app.py находящийся в папке backend:
```bash
python backend/app.py
```

После успешного запуска Веб-Интерфейса переходим по адресу:
```bash
http://127.0.0.1:5000/
```

### Авторы:
Савенков Дмитрий, Дарья Лоткова МПИ-23-1-2