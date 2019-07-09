import random
import time

class kumanda():
    def __init__(self,tv_durumu="kapalı",tv_ses=0,kanal_listesi="trt",kanal="trt",mute_durumu="off"):
        self.tv_durumu=tv_durumu
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        self.mute_durumu=mute_durumu


    def tv_aç(self):
        if(self.tv_durumu=="açık"):
            print("tv zaten açık")
        else:
            print("tv açılıyor....")
            time.sleep(1)
            self.tv_durumu="açık"

    def tv_kapa(self):
        if(self.tv_durumu=="kapalı"):
            print("tv zaten kapalı")
        else:
            print("tv kapatılıyor....")
            time.sleep(1)
            self.tv_durumu="kapalı"
    def ses_ayarı(self):
        while True:
            cevap=input("sesi açmak için: '>' yazınınz\nsesi kısmak için: '<' yaznınz\nçıkış yapmak için 'q' yazınız")
            if(cevap=='<'):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("ses.",self.tv_ses)
            elif(cevap=='>'):
                if(self.tv_ses!=32):
                    self.tv_ses+=1
                    print("ses:",self.tv_ses)
            else:
                print("çıkış yapılıyor")
                time.sleep(1)
                print("güncel ses:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor....")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("mevcut kanal:",self.kanal)

    def mute(self):
        mute_activate=input("mute aktif etmek için 'on' yazınınz")
        if(mute_activate=='on'):
            self.mute_durumu="on"
            print("mute aktif")


    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "tv durumu {}\nses durumu {}\nkanal listesi {}\nmevcut kanal {}\nmute: {}".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal,self.mute_durumu)



kontrol=kumanda()



print("""
                kumanda menüsü
                
    1.tv aç
    2.tv kapa
    3.ses ayarları
    4.kanal ekle
    5.kanal sayısını öğrenme
    6.rastegele kanal seçme
    8.mute durumu
    7.tv bilgileri
    
    çıkmak için 'exit' yaznınz
    
""")

while True:
    işlem=input("işlemi seçiniz")
    if(işlem!='1'):
        print("tv kapalıyken işlem yapılamaz")
    else:
        if(işlem=='exit'):
            print("program sonlanıyor....")
            break
        elif(işlem=='1'):
            kontrol.tv_aç()
        elif(işlem=='2'):
            kontrol.tv_kapa()
        elif(işlem=='3'):
            kontrol.ses_ayarı()
        elif(işlem=='4'):
            kanal_isimleri=input("kanal isimlerini ',' ile ayırınız")
            kanal_listesi=kanal_isimleri.split(",")
            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)
        elif(işlem=='5'):
            print("kanal sayısı",len(kontrol))
        elif(işlem=='6'):
            kontrol.rastgele_kanal()
        elif(işlem=='7'):
            print(kontrol)
        elif(işlem=='8'):
            kontrol.mute_durumu()
        else:
            print("geçersiz işlem")