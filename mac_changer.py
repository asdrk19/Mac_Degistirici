import subprocess #subprocess kütüphanesi yazdığımız kodları terminalde çalıştırmaya yarar.
import optparse #kullanıcıdan veri alıp program içinde kullanmamızı sağlayan kütüphane
import re

def kullanicidan_veriAl():
    parse_nesnesi = optparse.OptionParser()
    parse_nesnesi.add_option("-i","--interface",dest="arayuz",help="Değiştirilecek arayüzü girin") #kullanıcı -i yazıp değiştirmek istediği arayüzü giricek örn:eth0
    parse_nesnesi.add_option("-m","--mac",dest="mac_adresi",help="Istediginiz mac adresini girin") #kullanıcı -mac yazıp yeni mac adresini girecek.

    return parse_nesnesi.parse_args() #Kullanıcının girdiği verileri döndürüyoruz.
      #(kullanicinin_girdigi_veriler,Veri)=parse_nesnesi.parse_args() #bir değişkene parse kütüphanesinde oluşturduğumuz nesnenin özelliklerini kütüphanein parse.args() özelliğini kullanarak atıyoruz.

      #Degisecek_arayuz=kullanicinin_girdigi_veriler.arayuz #yukarda dest=arayuz olarak tanımladığımız kullanıcıdan alınan veriyi çekiyoruz.
      #YeniMac_adresi=kullanicinin_girdigi_veriler.mac_adresi #kullanıcıdan alınan mac adresini YeniMac_adresi 'ne atıp aşşağıda kulanıyoruz.


def mac_Adresi_Degis(Degisecek_arayuz, YeniMac_adresi):
    subprocess.call(["ifconfig", Degisecek_arayuz,"down"])    # terminalde yazdığımız kodları programla yazdırıyoruz.(eth'ı kapat.) eth0 yerine girilen değişken geldi.
    subprocess.call(["ifconfig", Degisecek_arayuz, "hw", "ether",YeniMac_adresi])    # Sanki terminal üstünde mac değiştiryorumuşuz gibi (eth'ın macini bununla değiş)
                                                                                     # terminalde yazdığımız şeyleri aynen yazıyoruz.
    subprocess.call(["ifconfig", Degisecek_arayuz, "up"])  # eth0'ı aç

    print(Degisecek_arayuz, "'ın mac adresi", YeniMac_adresi, "olarak güncellendi..")



def kontrol(arayuzz):

    kontrol_degisken = subprocess.check_output(["ifconfig",arayuzz])
    yeni_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(kontrol_degisken)) #mac adresinin içinde bu formatta veri arıyoruz.
    if yeni_mac: #eğer veri bulunursa
        return yeni_mac.group(0) #bulunan veriyi string olarak döndürme komutu. özel komut.
    else:
        return None

print("hello hacker!!")
(kullanicidan,veri) = kullanicidan_veriAl() #verileri almak için bir değişkem oluşturmalıyız.
mac_Adresi_Degis(kullanicidan.arayuz,kullanicidan.mac_adresi) #oluşturğumuz değişkene çekilen fonksiyonun içinde tanımladığımız arayuz ve mac_adresi verisini diğer fonksiyona gönderiyoruz.
final_mac = kontrol(str(kullanicidan.arayuz))

if final_mac == kullanicidan.mac_adresi:
    print("Mac değiştirme başarılı..")
else:
    print("İşlem başarısız!!")














# İlk program 18.03.2023 17:40 Hayır ve güzelliklere vesile olsun inşAllah...
