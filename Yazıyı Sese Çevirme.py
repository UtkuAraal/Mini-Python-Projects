from gtts import gTTS
from playsound import playsound


message = "Hello Utku"
speech = gTTS(text = message)
speech.save("text.mp3")
playsound("text.mp3")