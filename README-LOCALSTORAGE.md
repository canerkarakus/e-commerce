# LocalStorage Sorunları ve Çözümleri

## QuotaExceededError Hatası

Bu hata localStorage kapasitesinin dolması nedeniyle oluşur. Çözüm yöntemleri:

### 1. Tarayıcı Konsolundan Temizleme

Tarayıcıda F12 tuşuna basın ve Console sekmesinde şu komutları çalıştırın:

```javascript
// Tüm localStorage'ı temizle
localStorage.clear();

// Sadece siparişleri temizle
localStorage.removeItem('allOrders');

// LocalStorage boyutunu kontrol et
console.log('LocalStorage boyutu:', JSON.stringify(localStorage).length, 'karakter');

// Siparişleri kontrol et
console.log('Mevcut siparişler:', localStorage.getItem('allOrders'));
```

### 2. Admin Panelinden Temizleme

1. Admin hesabı ile giriş yapın (`admin@canerkarakus.com.tr`)
2. Admin paneline gidin
3. "Eski Siparişleri Temizle" butonuna tıklayın
4. Onaylayın

### 3. Manuel Tarayıcı Temizleme

**Chrome:**
1. F12 > Application sekmesi
2. Storage > Local Storage > localhost:3000
3. Sağ tık > Clear

**Firefox:**
1. F12 > Storage sekmesi
2. Local Storage > localhost:3000
3. Sağ tık > Delete All

### 4. Otomatik Çözümler

Sistem artık otomatik olarak:
- Sadece son 50 siparişi saklar
- 30 günden eski siparişleri temizler
- LocalStorage hatalarını yakalar ve düzeltir

## Önleme

- Düzenli olarak eski siparişleri temizleyin
- Test siparişleri verirken çok fazla sipariş vermeyin
- Geliştirme sırasında localStorage'ı düzenli temizleyin

## Hata Devam Ederse

1. Tarayıcıyı tamamen kapatın
2. Tarayıcı cache'ini temizleyin
3. Gizli/özel pencerede test edin
4. Farklı tarayıcıda test edin 