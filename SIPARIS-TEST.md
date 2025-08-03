# Sipariş Sistemi Test Talimatları

## 1. LocalStorage Temizleme

Tarayıcı konsolunda (F12 > Console) şu komutları çalıştırın:

```javascript
// Eski localStorage'ı temizle
localStorage.removeItem('orders');
localStorage.removeItem('allOrders');
localStorage.clear();

// Temizlendiğini kontrol et
console.log('LocalStorage temizlendi:', localStorage.length);
```

## 2. Test Adımları

### Adım 1: Giriş Yap
- `info@canerkarakus.com.tr` ile giriş yapın
- Console'da logları kontrol edin

### Adım 2: Sipariş Ver
1. Ana sayfada bir ürünü sepete ekleyin
2. Sepet sayfasına gidin
3. Checkout yapın (adres seçin)
4. Ödemeyi tamamlayın
5. Console'da şu logları kontrol edin:
   - "OrderContext: Yeni sipariş oluşturuluyor"
   - "LocalStorage'a başarıyla kaydedildi"

### Adım 3: Sipariş Kontrolü
1. Siparişler sayfasına gidin (`/orders`)
2. Siparişinizin görünüp görünmediğini kontrol edin
3. Console'da logları kontrol edin

### Adım 4: Çıkış/Giriş Testi
1. Çıkış yapın
2. Tekrar giriş yapın
3. Siparişler sayfasına gidin
4. Siparişinizin hala orada olup olmadığını kontrol edin

### Adım 5: Admin Kontrolü
1. `admin@canerkarakus.com.tr` ile giriş yapın
2. Admin paneline gidin
3. "Kullanıcı Siparişleri" butonuna tıklayın
4. Kullanıcının verdiği siparişin görünüp görünmediğini kontrol edin

## 3. Debug Komutları

Console'da kullanabileceğiniz komutlar:

```javascript
// Tüm siparişleri görüntüle
console.log('Tüm siparişler:', JSON.parse(localStorage.getItem('allOrders') || '[]'));

// LocalStorage boyutunu kontrol et
console.log('LocalStorage boyutu:', JSON.stringify(localStorage).length, 'karakter');

// Belirli kullanıcının siparişlerini filtrele
const allOrders = JSON.parse(localStorage.getItem('allOrders') || '[]');
const userOrders = allOrders.filter(order => order.userEmail === 'info@canerkarakus.com.tr');
console.log('Kullanıcı siparişleri:', userOrders);
```

## 4. Beklenen Sonuçlar

✅ Sipariş oluşturulduğunda localStorage'a kaydedilmeli
✅ Çıkış/giriş sonrası siparişler korunmalı
✅ Admin panelinde tüm siparişler görünmeli
✅ Kullanıcı sadece kendi siparişlerini görmeli
✅ Console'da hata olmamalı

## 5. Sorun Giderme

Eğer sorun devam ederse:

1. Tarayıcıyı tamamen kapatın
2. Cache'i temizleyin
3. Gizli pencerede test edin
4. Console'daki hata mesajlarını kontrol edin 