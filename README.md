# unfollow
Python3 ile yazıldı, instagramdan takipçi çıkartmayı sağlıyor

Programı sanal çalışma alanı oluşturup orada çalıştırırsanız daha sağlıklı olur. (Kullanım: http://kenanyaman.com/linux/python-calisma-ortami/)

Sanal ortam oluşturduktan sonra gerekli bağımlılıkları pip install -r requirements.txt ile kuruyoruz. Bağımlılıkları yükledikten sonra
python3 main_unfollow.py koduyla programı başlatıyoruz. Macos, windows ve linuxte çalışıyor. 

Çalışma mantığı: 
Hesap bilgilerinizi programa giriyorsunuz, Hesaplar klasörü oluşturuluyor ve içine txt formatında bilgiler kayıt ediliyor (şifreler açık bir şekilde kayıt ediliyor bunu göz önünde bulundurarak kullanın programı)
sonrasında program Google Chrome başlatıyor instagrama giriş yapıyor (verdiğiniz bilgiler ile) profil sayfasına gidiyor ve takipçileri tek tek çıkarmaya başlıyor.
Bu işlem arka planda oluyor, bunu görmek isterseniz eğer, 54. satırdaki kodun (self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)) içinden  chrome_options satırının çıkarın.
Bu şekilde canlı olarak programın ne yaptığının görebilirsiniz.


Program çalışmak için Google Chrome ihtiyaç duyuyor. Eğer Google Chrome u farklı bir dizine kurduysanız bunu config.py dosyasından düzeltip öyle programı çalıştırın
