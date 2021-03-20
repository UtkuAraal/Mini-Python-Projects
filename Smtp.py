import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "89D5C9@gmail.com"
mesaj["To"] = "utkuaraal1@gmail.com"
mesaj["Subject"] = "Smtp Mail Gönderme"
yazi = """
Smtp ile mail projesi.
Utku Araal
"""

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
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()
