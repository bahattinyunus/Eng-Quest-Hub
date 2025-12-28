# Katkıda Bulunma Rehberi

Eng-Quest-Hub projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Bu proje, hepimizin ortak bilgi havuzu olarak büyümeyi hedeflemektedir.

## Nasıl Katkı Sağlayabilirsiniz?

1. **Yeni Bir Etkinlik Duyurusu**: Gözünüze çarpan bir yarışma, hackathon veya kariyer fuarı varsa listeye ekleyin.
2. **Dokümantasyon**: Rapor yazım rehberleri, tecrübe paylaşımları veya ipuçları ekleyin.
3. **Hata Düzeltme**: Kırık linkleri veya yanlış tarihleri düzeltin.

## Teknik Katkı Rehberi: Etkinlik Ekleme

Bu repo, "Infrastructure as Code" mantığıyla yönetilmektedir. Etkinlikler doğrudan `README.md` dosyasına yazılmaz.

### Adım Adım Etkinlik Ekleme
1.  `data/events.json` dosyasını açın.
2.  `events` listesine yeni bir obje ekleyin. Şablon:
    ```json
    {
      "name": "Etkinlik Adı",
      "type": "Competition / Hackathon / Grant / Career Fair",
      "deadline": "YYYY-MM-DD",
      "date": "YYYY-MM-DD (Etkinlik günü)",
      "url": "https://resmi-site-linki.com",
      "tags": ["Tag1", "Tag2"],
      "status": "Confirmed (Kesinleşti) / Open (Başvuru Açık) / Predicted (Tahmini)"
    }
    ```
3.  Değişikliği yaptıktan sonra terminalde `python scripts/update_events.py` komutunu çalıştırarak çıktıyı kontrol edin.
4.  Çıktı düzgünse ve JSON hatası yoksa commit atabilirsiniz.

## Pull Request (PR) Süreci

1. Bu repoyu "Fork"layın.
2. Kendi bilgisayarınıza klonlayın (`git clone ...`).
3. Yeni bir dal (branch) oluşturun (`git checkout -b yeni-etkinlik-ekle`).
4. Değişikliklerinizi yapın (JSON dosyasını güncelleyin).
5. Değişikliklerinizi kaydedin (`git commit -m "feat: data_med_x hackathon eklendi"`).
6. Reponuza gönderin (`git push origin yeni-etkinlik-ekle`).
7. Bize bir "Pull Request" (PR) gönderin.

## Kurallar

* Eklediğiniz etkinliklerin tarihinin güncel olduğundan emin olun.
* Resmi kaynak linkini mutlaka ekleyin.
* Argo veya saygısız ifadelerden kaçının.

Teşekkürler! 🚀
