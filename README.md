🛍️ Web Alışveriş
Web Alışveriş, kullanıcıların ürünleri keşfedip satın alabileceği, satıcıların ise mağazalarını yönetebileceği modern bir e-ticaret platformudur.

🔐 Özellikler
👤 Kullanıcılar kayıt olabilir, giriş yapabilir ve tercihlerini güncelleyebilir

🔐 Tüm kullanıcı verileri güvenli bir şekilde saklanır

📦 Kullanıcılar sipariş verebilir, verilen siparişlerin durumu admin tarafından güncellenebilir

📧 Sipariş durumu güncellendiğinde hem kullanıcıya hem de adminde e-posta bildirimi gider

🛒 Satıcılar için özel bir dashboard vardır:

➕ Ürün ekleme

📝 Ürün düzenleme

🗑️ Ürün silme

🏪 Satıcı sayfası oluşturulabilir

📝 Satıcı olmak isteyenler talep formu doldurur

✅ Admin onaylarsa, mağaza açılır ve satış yapabilirler

✉️ E-posta Ayarları
E-posta gönderimi opsiyoneldir. Bu ayarlar olmadan da sistem çalışır, sadece e-posta bildirimleri gönderilmez.

📄 .env Dosyası Oluşturma
Proje kök dizininde .env.local dosyasını aşağıdaki gibi oluşturun:

env
Kopyala
Düzenle
# E-posta Ayarları (Opsiyonel)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
⚙️ Gmail Ayarları
🔐 Gmail hesabınızda 2 Adımlı Doğrulama'yı etkinleştirin

👤 Hesap > Güvenlik > 2 Adımlı Doğrulama > Uygulama Şifreleri

✨ "Web Alışveriş" için bir uygulama şifresi oluşturun

🔑 Bu şifreyi .env.local dosyasında SMTP_PASS olarak kullanın

📡 Diğer E-posta Sağlayıcıları
Sağlayıcı	SMTP Host ve Port
Outlook	smtp-mail.outlook.com:587
Yahoo	smtp.mail.yahoo.com:587
Yandex	smtp.yandex.com:587

🧪 Test Etme
E-posta ayarları doğru yapılandırıldıysa:

✅ Sipariş verildiğinde onay e-postası gelir

🔄 Sipariş durumu değiştiğinde bildirim e-postası gider

❌ Sipariş iptal edilirse yine bildirim e-postası gönderilir

⚠️ E-posta ayarları yapılmazsa sistem çalışmaya devam eder, yalnızca e-posta bildirimleri gönderilmez.
