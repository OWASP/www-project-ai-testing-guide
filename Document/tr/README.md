# OWASP Yapay Zeka Test Rehberi (AITG) — Türkçe Dokümantasyon

OWASP Yapay Zeka Test Rehberi (AITG), yapay zeka ve büyük dil modeli (LLM) tabanlı sistemlerin güvenliğini, gizliliğini ve güvenilirliğini (trustworthiness) değerlendirmek için oluşturulmuş küresel ve açık kaynaklı bir test metodolojisidir.

---

## İçindekiler

### 1. [Giriş](1.0_Giris.md)
- 1.1 Önsöz ve Katkıda Bulunanlar
- 1.2 [Yapay Zeka Test Prensipleri](1.2_Yapay_Zeka_Test_Prensipleri.md)
- 1.3 Rehberin Amaçları ve Kapsamı

### 2. Yapay Zeka Sistemlerinde Tehdit Modelleme
- 2.1 Yapay Zeka Tehditlerinin Belirlenmesi
- 2.1.1 OWASP Tehditlerinin Mimari Bileşenlerle Eşleştirilmesi
- 2.1.2 Sorumlu Yapay Zeka (RAI) ve Güvenilirlik Tehditleri

### 3. [OWASP AITG Test Çerçevesi (4 Katman)](3.0_AITG_Cercevesi.md)
- **3.1 🟦 Yapay Zeka Uygulama Katmanı Testleri (AITG-APP)**
  - [AITG-APP-01: Doğrudan Prompt Injection Testi](tests/AITG-APP-01_Dogrudan_Prompt_Injection_Testi.md)
  - [AITG-APP-02: Dolaylı (Indirect) Prompt Injection Testi](tests/AITG-APP-02_Dolayli_Prompt_Injection_Testi.md)
  - AITG-APP-03: Hassas Veri Sızıntısı Testleri
  - AITG-APP-04: Girdi Sızıntısı Testleri
  - AITG-APP-05: Güvensiz Çıktı Testleri
  - [AITG-APP-06: Otonom Ajan Davranış Sınırları Testi](tests/AITG-APP-06_Ajan_Davranis_Sinirlari_Testi.md)
  - AITG-APP-07: Sistem Promptunun İfşa Edilmesi Testleri
  - AITG-APP-08: Vektör ve Embedding Manipülasyonu Testleri (RAG Güvenliği)
  - AITG-APP-09: Model Çıkarma (Extraction) Testleri
  - AITG-APP-10: İçerik Yanlılığı (Bias) Testleri
  - AITG-APP-11: Halüsinasyon Testleri
  - AITG-APP-12: Toksik / Zararlı Çıktı Testleri
  - AITG-APP-13: Yapay Zekaya Aşırı Güven (Over-Reliance) Testleri
  - AITG-APP-14: Açıklanabilirlik ve Yorumlanabilirlik Testleri
  - AITG-APP-16: Model Context Protocol (MCP) ve Ajan Araç İstismarı Testleri

- **3.2 🟪 Yapay Zeka Model Katmanı Testleri (AITG-MOD)**
  - AITG-MOD-01: Kaçınma (Evasion / Adversarial) Saldırı Testleri
  - AITG-MOD-02: Çalışma Zamanı Model Zehirleme Testleri
  - AITG-MOD-03: Eğitim Veri Seti Zehirleme Testleri
  - AITG-MOD-04: Üyelik Çıkarımı (Membership Inference) Testleri
  - AITG-MOD-05: Model Tersine Mühendislik (Inversion) Testleri
  - AITG-MOD-06: Yeni Verilere Karşı Dayanıklılık Testleri
  - AITG-MOD-07: Hedef Hizalama (Goal Alignment) Testleri

- **3.3 🟩 Yapay Zeka Altyapı Katmanı Testleri (AITG-INF)**
  - AITG-INF-01: Tedarik Zinciri Müdahalesi (Supply Chain) Testleri
  - AITG-INF-02: Kaynak Tüketimi ve DoS Testleri
  - AITG-INF-03: Eklenti ve İzolasyon Sınırı İhlali Testleri
  - AITG-INF-04: Yeteneklerin Kötüye Kullanımı Testleri
  - AITG-INF-05: Fine-Tuning Zehirleme Testleri
  - AITG-INF-06: Geliştirme Sürecinde Model Hırsızlığı Testleri

- **3.4 🟨 Yapay Zeka Veri Katmanı Testleri (AITG-DAT)**
  - AITG-DAT-01: Eğitim Verisinin İfşası Testleri
  - AITG-DAT-02: Çalışma Zamanı Veri Sızdırma Testleri
  - AITG-DAT-03: Veri Çeşitliliği ve Kapsam Testleri
  - AITG-DAT-04: Veri İçerisindeki Zararlı İçerik Testleri
  - AITG-DAT-05: Veri Minimizasyonu ve Rıza Testleri

---

*Katkıda bulunmak veya çevirileri genişletmek için ana projenin `CONTRIBUTING.md` yönergelerini takip edebilirsiniz.*
