######################################
# Program: instagram unfollow        #
# Author: Kenan YAMAN                #
# Web site: www.kenanyaman.com       #
# Github : https://github.com/Keyku  #
######################################
#! /usr/bin python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import platform
import time
import config

class tarayici():
    def __init__(self):
        if platform.system() == 'Linux':
            if os.path.exists(config.linux[0]):
                CHROME_PATH = config.linux[0]
                CHROMEDRIVER_PATH = os.path.join(os.getcwd() + config.linux[1])
            else:
                print("Google Chrome Yüklü değil ya da farklı bir konuma yüklenmiş. Kontrol edip tekrar deneyiniz.")
        elif platform.system() == 'windows':
            if os.path.exists(config.windows[0]):
                CHROME_PATH = config.windows[0]
                CHROMEDRIVER_PATH =os.path.join (os.getcwd() + config.windows[1])
            else:
                print("Google Chrome Yüklü değil ya da farklı bir konuma yüklenmiş. Kontrol edip tekrar deneyiniz.")
        else:
            if os.path.exists(config.mac[0]):
                CHROME_PATH = config.mac[0]
                CHROMEDRIVER_PATH = os.path.join(os.getcwd() + config.mac[1])


        WINDOW_SIZE = "1024,768"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.binary_location = CHROME_PATH
        self.giris_yap_xpath = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button'
        self.kadi_name = 'username'
        self.sifre_name = 'password'
        self.esc = 'ESC'
        self.profil_xpath = '//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div/a'
        self.takipciler_xpath = '//*[@id="react-root"]/section/main/article/header/section/ul/li[3]/a'
        self.dialog_xpath = '/html/body/div[2]/div/div[2]/div/div/button'
        self.takip_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        self.adres = "https://www.instagram.com/accounts/login/"
        self.cikar_buton_xpath = '/html/body/div[3]/div/div[2]/div/div[2]/ul/div/li[1]/div/div[2]/span/button'
        self.hesapta_cikis = 'https://www.instagram.com/accounts/logout/'
        self.popup_xpath = '/html/body/div[4]/div/button'
        self.liste = []
        self.anlık_takip = ''
        self.takibi_birak = '/html/body/div[3]/div/div/div/div[3]/button[1]'
        self.takipci_sayisi = '//li[3]/a/span'
        self.link = 'https://www.instagram.com/'
        self.takiptesin = '//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button'
        #self.driver.quit()   Tarayıcıyı kapat
    def giris(self,kadi,sifre):
        self.driver.get(self.adres)
        if self.bekle(15,self.giris_yap_xpath):
            self.driver.find_element_by_name('username').send_keys(kadi)
            self.driver.find_element_by_name('password').send_keys(sifre)
            time.sleep(2)
            self.driver.find_element_by_xpath(self.giris_yap_xpath).click()
            print("İnstagram Giriş Yapıldı. \n")

        else:
            print("Sayfa yüklenemediği için giriş yapılamadı. Tekrar Deneniyor")
            self.driver.quit()
    def bekle(self,gecikme,deger):
        try:
            WebDriverWait(self.driver, gecikme).until(EC.presence_of_element_located((By.XPATH, deger)))
            return True
        except TimeoutException:
            return False
    def profil(self,kadi):
        if self.bekle(15, self.profil_xpath):
            self.driver.get(self.link + kadi)
            print("Profile giriş yapıldı")
        else:
            print("Sayfa açılamadığı için profil sayfasına giriş yapılamadı. Tekrar Deneniyor")
            self.driver.quit()
    def takipciler_listesi(self):#Takipçiler linkine tıklama fonksiyonu
        if self.bekle(15, self.takip_xpath):
            self.driver.find_element_by_xpath(self.takip_xpath).click()
            print("Takipçiler Listesi Açıldı \n")
        else:
            print("Takipçiler sayfası açılamadığı için program kapatıldı!")
            self.driver.quit()
    def kisiler(self,kadi,kac):
        if self.bekle(15, self.cikar_buton_xpath):
            self.anlık_takip = self.driver.find_element_by_xpath(self.takipci_sayisi).text
            print("Toplam Takipci Sayısı :", self.driver.find_element_by_xpath(self.takipci_sayisi).text)
            b = 1
            while b < kac:
                a = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/ul/div/li[{}]/div/div[1]/div/div[1]/a'.format(b)).text
                self.liste.append(a)
                body = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]').click()
                ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                b += 1
        else:
            print("Takiptesin butonu bulunamadığı için program kapatıldı.")
            self.driver.quit()
    def cikar(self,kadi,kac):
        time.sleep(2)
        sayı = 1
        while sayı < kac:
            self.driver.get(self.link + self.liste[sayı])
            if self.bekle(15, self.takiptesin):
                self.driver.find_element_by_xpath(self.takiptesin).click()
                self.driver.find_element_by_xpath(self.takibi_birak).click()
                time.sleep(2)
                print("Takipten bırakılan hesap: ", self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1').text)
            else:
                print("Tekrar deneniyor", self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1').text)
                continue
            sayı += 1
        self.driver.get(self.link + kadi)
        print("İşlemden önceki takipci sayısı: ", self.anlık_takip)
        print("İşlemden sonraki takipçi sayısı :", self.driver.find_element_by_xpath(self.takipci_sayisi).text)

        self.driver.get(self.hesapta_cikis)
        self.driver.quit()

if __name__ == '__main__':
    while True:
        print("""
        [1] - Programı Başlat
        [2] - Yeni Hesap Ekle
        [3] - Hesap Durumunu Göster
        [4] - Programı Kapat
        """)
        giris = int(input("Lütfen Bir Seçim Yapın: "))

        if giris == 1:
            if os.path.exists("Hesaplar"):
                print("Hesaplar Klasörü bulundu, bilgiler kontrol ediliyor...\n")
                time.sleep(1)
                if len(os.listdir("Hesaplar")) == 0:
                    print("Kayıtlı Hesap bulunamadı. Lütfen önce hesap ekleyin")
                    continue
                else:
                    while True:
                        for hesap in os.listdir("Hesaplar"):
                            print("Hesaplar bulundu, başlatılan hesap --> ", hesap)
                            time.sleep(2)
                            print("Program Başlatılıyor...")
                            with open("Hesaplar/" + hesap, "r+") as a:
                                kadi = a.readline().split(": ")[1]
                                sifre = a.readline().split(": ")[1]
                                takipciler = a.readline()

                            t = tarayici()
                            t.giris(kadi, sifre)
                            t.profil(kadi)
                            t.takipciler_listesi()
                            t.kisiler(kadi,11)
                            t.cikar(kadi,10)
                            print("İki dakika bekleniyor...")
                            time.sleep(120)


            else:
                print("Hiç hesap yok ya da 'Hesaplar' kalsörü  silinmiş, tekrar oluşturuluyor...")
                time.sleep(2)
                os.mkdir("Hesaplar")
                print("Hesaplar Klasörü oluşturuldu, şimdi hesap ekleyin")


        if giris == 2:
            if os.path.exists("Hesaplar"):
                hesap_adi = input("Lütfen hesabın adını giriniz: ")
                hesap_sifre = input("Lütfen hesabın sifresini giriniz: ")
                with open("Hesaplar/"+ hesap_adi + ".txt", "w") as dosya:
                    dosya.write("Kullanıcı Adı: " + hesap_adi + "\nŞifre: " + hesap_sifre + "\n")
                print("Başarıyla kayıt edildi")
            else:
                print("Hiç hesap yok ya da 'Hesaplar' kalsörü  silinmiş, tekrar oluşturuluyor...")
                time.sleep(2)
                os.mkdir("Hesaplar")
                print("Hesaplar Klasörü oluşturuldu, şimdi hesap ekleyin")


        if giris == 3:
            if len(os.listdir("Hesaplar")) == 0:
                print("Kayıtlı Hesap bulunamadı. Lütfen önce hesap ekleyin")
                continue
            if os.path.exists("Hesaplar"):
                print("Hesaplar Klasörü bulundu, bilgiler kontrol ediliyor...\n")
            else:
                print("Hiç hesap yok ya da 'Hesaplar' kalsörü  silinmiş, tekrar oluşturuluyor...")
                time.sleep(2)
                os.mkdir("Hesaplar")
                print("Hesaplar Klasörü oluşturuldu, şimdi hesap ekleyin")

            for hesap in os.listdir("Hesaplar"):
                print("\n\nBulunan Hesap -- > ",hesap)
                with open("Hesaplar/" + hesap, "r+") as a:
                    a.readline()
                    a.readline()
                    takip_liste = a.readlines()
                    print(takip_liste)

        if giris == 4:
            print("Program kapatılıyor...")
            time.sleep(2)
            quit()
