# global saglik analizi ve stratejik icgoru raporu
Bu çalışma, dünya genelindeki sağlık verilerini analiz ederek; operasyonel büyüme trendlerini, bölgesel risk faktörlerini ve ürün etkileşiminin (UX) kullanıcı sağlığı üzerindeki etkilerini saptamak amacıyla hazırlanmıştır.
Kaggle'dan alınan 'kantesti_global_health_insights_2025_2026' veri seti kullanılmıstır.
 
işte yorumladığım bazı bulgular...


<img width="1536" height="762" alt="heatmap_new" src="https://github.com/user-attachments/assets/60aca696-2931-4c8c-8ec5-f65164554fde" />
Tablodaki en çarpıcı bulgular 45-59 yaş aralığında toplanmış durumda. Bu grup, kronik hastalıklarla en güçlü korelasyonu gösteriyor:

# Diyabet ve Anemi Patlaması:
Bu yaş grubunda diyabet (0.58) ve anemi (0.68) ile çok güçlü pozitif korelasyonlar var. Bu, sağlık politikalarının bu yaş grubunda tarama ve önleyici tedavilere odaklanması gerektiğini gösterir.

Sağlık Skoru Düşüşü: Aynı grubun avg_health_score ile korelasyonu -0.48. Yani bu yaş grubunun payı arttıkça, genel sağlık skoru belirgin şekilde düşüyor.

# Gençlerde Sağlık Skorunun Korunması (18-29 Yaş)
Negatif Anemi İlişkisi: 18-29 yaş grubu ile anemi arasında -0.41 gibi güçlü bir negatif korelasyon var. Genç nüfusun yoğun olduğu yerlerde anemi yaygınlığı daha düşük görünüyor.

Pozitif Sağlık Skoru: Beklendiği üzere, bu grubun sağlık skoru ile korelasyonu pozitif (0.32). Ancak bu rakamın çok daha yüksek olmaması, genç nüfusta da gizli risklerin (örneğin yaşam tarzı faktörleri) olabileceğini düşündürür.

# Yaşlı Nüfus (60+) ve Beklenmedik Bulgular
Kardiyovasküler Risk: 60+ yaş grubu ile kardiyovasküler durumlar arasında pozitif bir ilişki (0.27) var. Ancak şaşırtıcı olan, diyabet ve anemi ile olan korelasyonun negatif olması.
Bu durum yaşlı nüfusta bu hastalıkların olmadığı anlamına gelmez.

Diyabet, 45-59 Yaş,Erken teşhis programları bu gruba yönlendirilmeli.  
Anemi, 45-59 Yaş,Beslenme ve kan değerleri takibi bu yaşta kritik.  
Kardiyovasküler, 60+ Yaş,Kronik kalp sağlığı yönetimi yaşlı nüfusta öncelik.  
Genel Sağlık, 18-29 Yaş,Sağlık skorunu yükselten ana motor genç nüfus.  


# Global Test Hacmi ve MoM (Aydan Aya) Büyüme Analizi
Amacımız: Küresel sağlık veri setinin ivmesini ve hangi dönemlerde veri yoğunluğunun arttığını saptamak.
<img width="1400" height="700" alt="büyüme trendi" src="https://github.com/user-attachments/assets/dbaf8990-73a6-45a4-b2d8-8988e14ff93a" />
Ham test sayıları yanıltıcı olabilir. 100.000 test yapmak kulağa iyi gelebilir, ancak bir önceki ay 120.000 yaptıysanız bu bir alarmdır.

Mevsimsel Etki (Kırmızı Çizgi): Büyüme oranındaki (kırmızı çizgi) dalgalanmalar, insanların sağlık kontrolü yaptırma alışkanlıklarının mevsimselliğini gösterir. Örneğin; yılın belli aylarında test hacmi düşüyorsa, bu bize küresel ölçekte "sağlık bilincinin" dönemlere göre nasıl değiştiğini anlatır.

Kırmızı çizginin sıfırın altına düştüğü veya çok düşük kaldığı aylar, o dönemki sağlık verilerinin daha dar bir örneklemden geldiğini söyler. bu aylardaki sonuçlara daha temkinli yaklaşmamız gerekir.

# Bölgesel Sağlık Karnesi
<img width="1000" height="600" alt="Figure_3" src="https://github.com/user-attachments/assets/9e5493da-951b-4254-b6b4-f152aeb5217a" />

En Sağlıklı Bölge: Avrupa (72.24)
Neden? Avrupa'da diyabet ve metabolik sendrom oranları diğer bölgelere göre daha düşük seviyelerde. Sağlık bilincinin veya diyet alışkanlıklarının bu skoru yukarı çektiğini söyleyebiliriz.

En "Düşük Skorlu" Bölge: Güney Amerika (71.04)
Neden? Veride Güney Amerika'daki Anemi (Anemia) oranının (%31.89), Avrupa'nın (%19.08) neredeyse iki katı olduğunu görüyoruz. Bu ciddi bir beslenme veya demir eksikliği sorununa işaret ediyor ve genel sağlık puanını aşağı çekiyor.


# Bölgelerin "Kronik" Sorunları
<img width="1200" height="700" alt="bölgeleregöre" src="https://github.com/user-attachments/assets/8c08659b-02fc-4022-8421-bcd4c1b12188" />
# bölgelere göre anemi 
<img width="1000" height="600" alt="bölgeleregöreanemi" src="https://github.com/user-attachments/assets/cd4a7578-47cc-4b30-a01b-8eda00c11cb6" />

Avrupa'nın En Büyük Sorunu: Vitamin D  
Kuzey Amerika'nın En Büyük Sorunu: LDL Kolesterol (kötü kolestrol) genellikle yüksek yağlı beslenme ve yaşam tarzıyla ilişkilendirilen bir durum.  
Güney Amerika'nın En Büyük Sorunu: Ferritin (Demir Deposu) Bir önceki analizdeki yüksek anemi oranını burada "Ferritin" (demir deposu) anomalisiyle doğrulamış oluyoruz. Güney Amerika için en büyük sağlık önerisi "demir takviyesi ve beslenme düzeni" olacaktır.
