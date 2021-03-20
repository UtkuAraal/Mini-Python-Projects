import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound

url = "https://python-istihza.yazbel.com/kitap_hakkinda.html#bu-kitaptan-nasil-yararlanabilirim"
response = requests.get(url)
response_content = response.content
soup = BeautifulSoup(response_content, "html.parser")

metin = ""

for i in soup.find_all("p"):
    metin += i.text
    i = 0
    if i == 1:
        break
    i += 1
print(metin)
speech = gTTS(text = metin, lang="tr")
speech.save("Python_Belge.mp3")
playsound("Python_Belge.mp3")