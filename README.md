# RainMan Virtual Assistant

RainMan is a Python-based virtual assistant capable of performing various tasks such as answering questions, opening websites, playing music, fetching news, and more. It uses speech recognition and text-to-speech technologies for user interaction.

---

## Features
- **Voice Interaction**: Uses speech recognition (SpeechRecognition) to listen to commands and responds via text-to-speech (pyttsx3 or gTTS with pygame).
- **AI Assistance**: Integrates OpenAI for intelligent responses to user queries.
- **Web Integration**: Opens popular websites like Google, YouTube, Facebook, and LinkedIn.
- **Music Playback**: Plays songs from a predefined library (`musicLibrary.py`).
- **News Updates**: Fetches top news headlines using the NewsAPI.
- **Wake Word Detection**: Activates on hearing the wake word **"Rainman"**.
- **Stop Command**: Exits on hearing the word **"stop"**.

---

## Technologies Used
### Python Libraries:
- `SpeechRecognition`
- `pyttsx3`
- `gTTS`
- `pygame`
- `webbrowser`
- `requests`
- `openai`

### APIs:
- **OpenAI GPT API** for intelligent responses.
- **NewsAPI** for fetching the latest news headlines.

---

## Setup Instructions

### Prerequisites
- Ensure you have Python 3.7+ installed on your system.

### Install Dependencies
Run the following commands to install the required Python packages:
```bash
pip install speechrecognition pyaudio pyttsx3 setuptools webbrowser pocketsphinx openai gTTS pygame requests

