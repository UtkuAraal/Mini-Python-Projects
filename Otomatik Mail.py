import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

bilgiler = list()
with open("Mail_Gönderilecek.txt", "r", encoding="utf-8") as file:
    for i in file:
        bilgiler.append(i)
try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("utkuaraal1@gmail.com", "***")

    for i in range(0, len(bilgiler)):
        bilgiler[i] = bilgiler[i].split(",")

        mesaj = MIMEMultipart()

        mesaj["From"] = "utkuaraal1@gmail.com"
        mesaj["To"] = bilgiler[i][1]
        mesaj["Subject"] = "Bilgilendirme Maili"
        icerik = "Sayın " + bilgiler[i][0] + " bu bir bilgilendirme mailidir." + "\n\n\n\t\t\tUtku Araal"
        mail_govdesi = MIMEText(icerik, "plain")
        mesaj.attach(mail_govdesi)


        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print(bilgiler[i][0], "isimli mail sahibine mail ulaştırıldı.")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu ve " + bilgiler[i][0] +" isimli mail sahibine maili ulaştırılamadı!\n")
    sys.stderr.flush()


