import  smtplib
from email.mime.multipart  import  MIMEMultipart
from  email.mime.text import  MIMEText
import sys

adresler=list()

while True:
    posta_adresi=input("e posta göndermek istediğiniz adresi giriniz:\nçıkış için 'q' tuşuna basınız")

    if(posta_adresi== 'q'):
        print("çıkış yapıldı...")
        break
    else:
        adresler.append(posta_adresi)







mesaj=MIMEMultipart()

mesaj["From"]="pelezinhotolga@gmail.com"


mesaj["Subject"]="smtp mail gönderme"

yazı="""


smtp library ile birden fazla kişiye aynı mesajı göndermek

                            tolga em


"""


mesaj_gövdesi=MIMEText(yazı,"plain")

mesaj.attach(mesaj_gövdesi) #mesaj gövdemizi mesaj yapımıza ekliyoruz

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()  # smtp serverına kendimiz bağlıyoruz

mail.starttls()  # kullanıcı adı ve şifremizin encrypt edilmesi için
# bu iki komut mutlaka konulmalı

mail.login("", "")  # kullanıcı adı ve şifre girdisi için /kendi mail kullanıcı adınızı ve şifrenizi girmelisiniz

for i in adresler:

    try:
        mesaj["To"]=i


        mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

        print("mail başarıyla gönderildi....")


    except:
        sys.stderr.write("bir sorun oluştu")
        sys.stderr.flush()

mail.close() #smtp serverı ile bağlantıyı kesiyoruz







