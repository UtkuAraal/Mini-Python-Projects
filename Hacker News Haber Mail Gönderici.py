import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import sys

url = "https://news.ycombinator.com/"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

mesaj = MIMEMultipart()

mesaj["From"] = "89D5C9@gmail.com"
mesaj["To"] = "utkuaraal1@gmail.com"
mesaj["Subject"] = "Hacker News Haber Başlıkları"
yazi = ""

for i in soup.find_all("a", {"class": "storylink"}):
    yazi += i.text + "\n"

mesaj_govdesi = MIMEText(yazi, "plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("89D5C9@gmail.com", "***")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail Başarıyla Gönderildi.")
    mail.close()
except:
    sys.stderr.write("Bir hata oluştu!")
    sys.stderr.flush()

