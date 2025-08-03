#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WordPress Teması ZIP Oluşturma Script'i
WordPress'e doğrudan yüklenebilir tema ZIP'i oluşturur
"""

import os
import zipfile
import shutil
from pathlib import Path
from datetime import datetime

def create_wordpress_theme_zip():
    print("🎨 WordPress Teması ZIP dosyası oluşturuluyor...")
    
    # Mevcut dizin
    current_dir = Path.cwd()
    source_folder = current_dir / "modernshop-theme"
    
    # ZIP dosyası adı
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    zip_filename = f"modernshop-theme_{date_str}.zip"
    zip_path = current_dir / zip_filename
    
    print(f"📁 Kaynak klasör: {source_folder}")
    print(f"📦 ZIP dosyası: {zip_filename}")
    
    # Kaynak klasörün varlığını kontrol et
    if not source_folder.exists():
        print("❌ modernshop-theme klasörü bulunamadı!")
        return False
    
    # Gerekli dosyaların varlığını kontrol et
    required_files = ['style.css', 'index.php', 'functions.php']
    missing_files = []
    
    for file in required_files:
        if not (source_folder / file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Gerekli dosyalar eksik: {', '.join(missing_files)}")
        return False
    
    print("✅ Tema dosyaları kontrol edildi.")
    
    # Eski ZIP dosyasını sil (varsa)
    if zip_path.exists():
        zip_path.unlink()
        print("🗑️  Eski ZIP dosyası silindi.")
    
    try:
        print("📦 ZIP dosyası oluşturuluyor...")
        
        # ZIP dosyası oluştur - tema dosyalarını doğrudan root'a koy
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zip_obj:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    file_path = Path(root) / file
                    # ZIP içindeki path - modernshop-theme/ prefix'ini kaldır
                    relative_path = file_path.relative_to(source_folder)
                    zip_obj.write(file_path, relative_path)
                    print(f"  ➕ {relative_path}")
        
        # Dosya boyutunu göster
        file_size = zip_path.stat().st_size
        size_kb = round(file_size / 1024, 2)
        size_mb = round(file_size / (1024 * 1024), 2)
        
        print(f"✅ WordPress teması başarıyla oluşturuldu: {zip_filename}")
        print(f"📏 Dosya boyutu: {size_kb} KB ({size_mb} MB)")
        
        # İçeriği kontrol et
        print("\n📋 Tema dosyaları:")
        entry_count = 0
        with zipfile.ZipFile(zip_path, 'r') as zip_obj:
            for name in sorted(zip_obj.namelist()):
                if not name.endswith('/'):  # Klasörleri hariç tut
                    print(f"  📄 {name}")
                    entry_count += 1
        
        # WordPress'e yükleme talimatları
        print(f"\n📊 Tema İstatistikleri:")
        print(f"  📁 Toplam dosya sayısı: {entry_count}")
        print(f"  📦 Tema boyutu: {size_mb} MB")
        print(f"  🕒 Oluşturulma zamanı: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
        
        print(f"\n🎯 WordPress Kurulum Talimatları:")
        print(f"1. WordPress admin paneline giriş yapın")
        print(f"2. Görünüm > Temalar > Yeni Ekle")
        print(f"3. 'Tema Yükle' butonuna tıklayın")
        print(f"4. '{zip_filename}' dosyasını seçin")
        print(f"5. 'Şimdi Yükle' butonuna tıklayın")
        print(f"6. 'Etkinleştir' butonuna tıklayın")
        
        return True
        
    except Exception as e:
        print(f"❌ ZIP dosyası oluşturulurken hata: {e}")
        return False

if __name__ == "__main__":
    success = create_wordpress_theme_zip()
    if success:
        print("\n🎉 WordPress teması hazır!")
        print("📌 ZIP dosyasını doğrudan WordPress'e yükleyebilirsiniz.")
    else:
        print("\n💥 İşlem başarısız oldu!")
        exit(1) 