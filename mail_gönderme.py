import  smtplib
from email.mime.multipart  import  MIMEMultipart
from  email.mime.text import  MIMEText
import sys

mesaj=MIMEMultipart()

mesaj["From"]="pelezinhotolga@gmail.com"   #mail gönderecek adres

mesaj["To"]="alirizacan7@gmail.com"   #mail gönderilecek adres

mesaj["Subject"]="smtp mail gönderme"

yazı="""


bu mail smtp modül ile gönderilmektedir

                            tolga em


"""


mesaj_gövdesi=MIMEText(yazı,"plain")

mesaj.attach(mesaj_gövdesi) #mesaj gövdemizi mesaj yapımıza ekliyoruz

try:
    mail=smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo() # smtp serverına kendimiz bağlıyoruz

    mail.starttls() # kullanıcı adı ve şifremizin encrypt edilmesi için
                    #bu iki komut mutlaka konulmalı

    mail.login("      ","    ") #kullanıcı adı ve şifre girdisi için / kendi mail adresinizi ve şifrenizi girmelisiniz

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("mail başarıyla gönderildi....")

    mail.close() #smtp serverı ile bağlantıyı kesiyoruz
except:
    sys.stderr.write("bir sorun oluştu")
    sys.stderr.flush()


