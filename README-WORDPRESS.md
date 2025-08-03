# WordPress Entegrasyonu

Bu proje artık **headless WordPress** entegrasyonu ile tam uyumlu hale getirilmiştir. WordPress admin panelinden kolayca sayfa ve içerik yönetimi yapabilir, mevcut Next.js sitenizi bozmadan WordPress'in gücünden yararlanabilirsiniz.

## 🎯 Özellikler

- ✅ **Headless WordPress** entegrasyonu
- ✅ Mevcut Next.js yapısını koruma
- ✅ WordPress admin panelinden kolay sayfa yönetimi
- ✅ Otomatik içerik senkronizasyonu
- ✅ CORS güvenlik ayarları
- ✅ Fallback içerik sistemi
- ✅ Modern admin paneli
- ✅ TypeScript tam desteği

## 🚀 Kurulum

### 1. Gereksinimler

- WordPress kurulumu (yerel veya uzak sunucu)
- Node.js 18+
- WP REST API aktif (WordPress 4.7+ ile varsayılan)

### 2. Hızlı Kurulum

```bash
# WordPress kurulum scriptini çalıştır
npm run wp:setup

# Paketleri yükle
npm install

# Uygulamayı başlat
npm run dev
```

### 3. Manuel Kurulum

#### WordPress Kurulumu
1. WordPress'i `http://localhost/wordpress` adresine kurun
2. WP Admin paneline giriş yapın

#### CORS Ayarları
WordPress temanızın `functions.php` dosyasına aşağıdaki kodu ekleyin:

```php
// CORS ayarları (WordPress functions.php dosyasına ekleyin)
function add_cors_http_header(){
    header("Access-Control-Allow-Origin: http://localhost:3000");
    header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
    header("Access-Control-Allow-Headers: Content-Type, Authorization");
}
add_action('init','add_cors_http_header');

// REST API için ek güvenlik
function custom_rest_cors() {
    remove_filter( 'rest_pre_serve_request', 'rest_send_cors_headers' );
    add_filter( 'rest_pre_serve_request', function( $value ) {
        header( 'Access-Control-Allow-Origin: http://localhost:3000' );
        header( 'Access-Control-Allow-Methods: GET, POST, OPTIONS' );
        header( 'Access-Control-Allow-Credentials: true' );
        return $value;
    });
}
add_action( 'rest_api_init', 'custom_rest_cors', 15 );
```

#### Environment Ayarları
`.env.local` dosyası oluşturun:

```env
# WordPress Entegrasyonu
NEXT_PUBLIC_WORDPRESS_URL=http://localhost/wordpress
```

## 📖 Kullanım

### WordPress Admin Paneli
1. Next.js uygulamanızı başlatın: `npm run dev`
2. Admin paneline giriş yapın: `/admin`
3. WordPress kartına tıklayın: `/admin/wordpress`
4. Bağlantı durumunu kontrol edin

### Sayfa Oluşturma
1. WordPress admin panelinden **Sayfalar > Yeni Ekle**
2. Sayfa başlığı ve içeriği yazın
3. Yayınla'ya tıklayın
4. Next.js'te görüntülemek için: `/wp-page/[sayfa-slug]`

### Blog Yazısı Oluşturma
1. WordPress admin panelinden **Yazılar > Yeni Ekle**
2. Yazı başlığı ve içeriği yazın
3. Yayınla'ya tıklayın
4. Next.js'te görüntülemek için: `/wp-post/[yazi-slug]`

## 🛠️ API Kullanımı

### WordPress Hook'ları
```tsx
import { useWordPress } from '@/context/WordPressContext';

function MyComponent() {
  const { 
    pages, 
    posts, 
    isConnected, 
    getPage, 
    getPost 
  } = useWordPress();
  
  // Sayfa getir
  const loadPage = async () => {
    const page = await getPage('hakkimizda');
    console.log(page);
  };
  
  // Yazı getir
  const loadPost = async () => {
    const post = await getPost('ilk-yazim');
    console.log(post);
  };
}
```

### WordPress Bileşenleri
```tsx
import WordPressPage from '@/components/WordPressPage';
import { WordPressPost } from '@/components/WordPressPage';

// Sayfa görüntüleme
<WordPressPage 
  slug="hakkimizda"
  fallbackContent={<div>Yükleniyor...</div>}
  showTitle={true}
/>

// Yazı görüntüleme
<WordPressPost 
  slug="ilk-yazim"
  showTitle={true}
  showMeta={true}
/>
```

## 🔧 Yapılandırma

### WordPress URL Değiştirme
`.env.local` dosyasında:
```env
NEXT_PUBLIC_WORDPRESS_URL=https://your-wordpress-site.com
```

### Özel Post Type'lar
```tsx
import { WordPressAPI } from '@/lib/wordpress';

// Özel post type getir
const products = await WordPressAPI.getCustomPosts('product', {
  per_page: 10,
  status: 'publish'
});
```

## 📱 URL Yapısı

| Tip | WordPress | Next.js |
|-----|-----------|---------|
| Sayfa | `/hakkimizda` | `/wp-page/hakkimizda` |
| Yazı | `/hello-world` | `/wp-post/hello-world` |
| Admin | `/wp-admin` | `/admin/wordpress` |

## 🔒 Güvenlik

- CORS ayarları ile güvenli API erişimi
- HTML içerik temizleme (DOMPurify)
- XSS koruması
- Sadece okuma yetkisi (GET istekleri)

## 🎨 Özelleştirme

### Tema Entegrasyonu
WordPress temanızda Next.js sayfalarına yönlendirme:

```php
// WordPress tema entegrasyonu
function redirect_to_nextjs($template) {
    if (is_page() || is_single()) {
        $post = get_queried_object();
        if ($post) {
            $nextjs_url = 'http://localhost:3000/wp-' . $post->post_type . '/' . $post->post_name;
            wp_redirect($nextjs_url);
            exit;
        }
    }
    return $template;
}
add_filter('template_include', 'redirect_to_nextjs');
```

### CSS Stilleri
WordPress içeriği için özel stiller:
```css
.wordpress-content {
  @apply prose prose-lg max-w-none;
}

.wordpress-content img {
  @apply rounded-lg shadow-md;
}
```

## 🧪 Test URL'leri

- WordPress REST API: `http://localhost/wordpress/wp-json/wp/v2/`
- Sayfalar: `http://localhost/wordpress/wp-json/wp/v2/pages`
- Yazılar: `http://localhost/wordpress/wp-json/wp/v2/posts`
- Medya: `http://localhost/wordpress/wp-json/wp/v2/media`

## 🚨 Sorun Giderme

### Bağlantı Sorunu
1. WordPress REST API'sinin aktif olduğunu kontrol edin
2. CORS ayarlarını kontrol edin
3. WordPress URL'sinin doğru olduğunu kontrol edin

### İçerik Görünmüyor
1. WordPress'te sayfa/yazının yayınlandığını kontrol edin
2. Slug'ın doğru olduğunu kontrol edin
3. Network sekmesinden API isteklerini kontrol edin

### CORS Hatası
1. `functions.php` dosyasına CORS kodunu ekleyin
2. WordPress'i yeniden başlatın
3. Tarayıcı cache'ini temizleyin

## 📦 Kullanılan Paketler

- `axios` - HTTP istekleri
- `graphql-request` - GraphQL sorguları
- `html-react-parser` - HTML parse işlemi
- `dompurify` - İçerik güvenliği
- `isomorphic-dompurify` - SSR desteği

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun: `git checkout -b feature/wordpress-enhancement`
3. Değişikliklerinizi commit edin: `git commit -am 'WordPress özelliği eklendi'`
4. Branch'inizi push edin: `git push origin feature/wordpress-enhancement`
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 💡 İpuçları

- WordPress admin panelinden düzenli olarak backup alın
- Performans için WordPress cache plugin'i kullanın
- SEO için Yoast SEO plugin'ini kurun
- Gelişmiş özellikler için Advanced Custom Fields kullanın

---

**Not:** Bu entegrasyon mevcut Next.js sitenizi hiç bozmaz. WordPress bağlantısı olmadığında site normal şekilde çalışmaya devam eder. 