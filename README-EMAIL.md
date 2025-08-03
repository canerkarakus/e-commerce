# E-posta Ayarları

E-posta gönderimi opsiyoneldir. Bu ayarlar olmadan da sistem çalışır, sadece e-posta bildirimleri gönderilmez.

## .env Dosyası Oluşturma

Proje kök dizininde `.env.local` dosyası oluşturun:

```env
# E-posta Ayarları (Opsiyonel)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
```

## Gmail Ayarları

1. Gmail hesabınızda 2 Adımlı Doğrulama'yı açın
2. Hesap > Güvenlik > 2 Adımlı Doğrulama > Uygulama Şifreleri
3. "E-Market" için uygulama şifresi oluşturun
4. Bu şifreyi `SMTP_PASS` olarak kullanın

## Diğer E-posta Sağlayıcıları

- **Outlook**: `smtp-mail.outlook.com:587`
- **Yahoo**: `smtp.mail.yahoo.com:587`
- **Yandex**: `smtp.yandex.com:587`

## Test Etme

E-posta ayarları doğru yapıldıysa:
- Sipariş verirken onay e-postası gelir
- Sipariş durumu değiştiğinde bildirim e-postası gelir
- Sipariş iptal edildiğinde bildirim e-postası gelir

E-posta ayarları yoksa sistem yine çalışır, sadece e-posta gönderilmez. 