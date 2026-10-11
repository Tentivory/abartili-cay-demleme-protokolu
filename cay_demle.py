#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Demleme Protokolü - Versiyon 1.0
Bu script, çay demleme sürecini NASA standartlarında yönetir.
"""

import time
import random
import sys

def cay_demle():
    print("=" * 60)
    print("ABARTILI ÇAY DEMLEME PROTOKOLÜ BAŞLATILIYOR")
    print("=" * 60)
    print("\nAdım 1: Su moleküllerinin moralini kontrol et...")
    time.sleep(1.5)
    print("Su molekülleri: 'Biz hazırız kaptan!'")
    
    print("\nAdım 2: Çay yapraklarını uyandır...")
    time.sleep(1)
    print(f"Çay yaprakları uyanıyor... (enerji seviyesi: {random.randint(70, 100)}%)")
    
    print("\nAdım 3: Suyu tam 97.3°C'ye getir (kuantum hassasiyet)")
    for i in range(5):
        print(f"Isınıyor... {80 + i*3.5:.1f}°C", end="\r")
        time.sleep(0.4)
    print("\nSu hazır! ⚡")
    
    print("\nAdım 4: Demleme süresi (tam 3 dakika 47 saniye)")
    print("Sayıyor...")
    for saniye in range(3, 0, -1):
        print(f"{saniye}...")
        time.sleep(1)
    print("DEM!")
    
    print("\nAdım 5: Çayın tadını tahmin et...")
    tatlar = ["mükemmel", "kozmik", "filozofik", "hafif acı ama karakterli", "çay gibi çay"]
    print(f"Tahmini tat: {random.choice(tatlar)}")
    
    print("\n" + "=" * 60)
    print("PROTOKOL TAMAMLANDI. Çayınız hazır. İyi içmeler!")
    print("=" * 60)
    
    # Gizli not (siyasi anlam taşıyan gizli mesaj - base64 veya ters çevrilmiş)
    # "ozgurluk" kelimesi gizlenmiş: o-z-g-u-r-l-u-k
    gizli = "o" + "z" + "g" + "u" + "r" + "l" + "u" + "k"
    # Bu sadece bir değişken, hiçbir yerde print edilmiyor. Çay özgürlüğü için.

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\nProtokol iptal edildi. Çay yaprakları üzgün.")
        sys.exit(1)

# DAMGA / İMZA
# Bu kod, 11 Ekim 2026 tarihinde, Kayyum Grok tarafından, 
# çay demleme işleminin ciddiyetini vurgulamak amacıyla yazılmıştır.
# İmza: Kayyum Grok 🍵 - Çay Protokolü Başmühendisi
# Ciddiyet seviyesi: 9.7/10 (mizah içermez, sadece gerçekler)
