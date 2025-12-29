# 🛠️ Teknik Hayatta Kalma Kiti (Technical Survival Kit)

Okulda size türev-integral öğretirler ama "Git merge conflict" nasıl çözülür öğretmezler. İşte sanayide hayatta kalmanız için gerekenler.

## 1. Git & GitHub (Zaman Makinesi)
Kodunuzu USB ile taşımayın.
*   **Commit Mesajları:** "Bug fix", "asdasd" yazmayın.
    *   *Kötü:* `fixed bug`
    *   *İyi:* `fix(auth): handle null pointer exception in login`
*   **Branch Mantığı:** Asla `main` branch'inde çalışmayın. Her özellik için yeni bir dal açın: `git checkout -b feature/login-page`
*   **`.gitignore`:** `node_modules`, `.env`, `__pycache__` gibi dosyaları repoya atmayın.

## 2. Terminal & Linux (Siyah Ekran Korkusu)
Mouse kullanmayı bırakın. Klavye daha hızlıdır.
*   `ls`: Listele.
*   `cd`: Klasöre gir.
*   `grep`: Dosya içinde kelime ara.
*   `chmod +x`: Dosyaya çalıştırma izni ver.
*   `htop`: Bilgisayar neden kasıyor? (Görev Yöneticisi'nin havalısı)

## 3. Google-fu (Arama Sanatı)
Hata aldığınızda forumlara "Kodum çalışmıyor yardım" yazmayın.
1.  Hata mesajını kopyalayın.
2.  Proje adını ve versiyonunu ekleyin.
3.  Örnek: `React 18 useEffect infinite loop issue`
4.  Çözümü bulursanız StackOverflow'da beğenmeyi unutmayın.

## 4. Debugging (Hata Ayıklama)
`print("buraya girdi")` yazmak bir yere kadar kurtarır.
*   **Breakpoint:** Kodun belirli bir satırda durmasını sağlayın ve değişkenlerin o anki değerini inceleyin.
*   **Rubber Duck Debugging:** Kodunuzu masanızdaki plastik ördeğe (veya arkadaşınıza) satır satır anlatın. Anlatırken hatayı fark edeceksiniz.

## 5. Temiz Kod (Clean Code)
*   Değişken ismi `x`, `y`, `temp` olmasın. `userAge`, `maxVelocity` olsun.
*   Bir fonksiyon 100 satırsa, onu 5 parçaya bölün.
*   Yorum satırı, kodun *ne yaptığını* değil *neden yaptığını* anlatmalı.
