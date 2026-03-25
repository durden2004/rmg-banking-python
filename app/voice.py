from gtts import gTTS
import uuid
import os

AUDIO_FOLDER = "audio"

if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)

def generate_voice(text: str):

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    tts = gTTS(text)
    tts.save(filepath)

    return filepath
