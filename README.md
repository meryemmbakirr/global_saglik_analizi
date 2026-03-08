# Global saglik analizi ve stratejik icgoru raporu
Bu çalışma, dünya genelindeki sağlık verilerini analiz ederek; operasyonel büyüme trendlerini, bölgesel risk faktörlerini ve ürün etkileşiminin (UX) kullanıcı sağlığı üzerindeki etkilerini saptamak amacıyla hazırlanmıştır.
Kaggle'dan alınan 'kantesti_global_health_insights_2025_2026' veri seti kullanılmıstır.

# değişkenleri  tanıyalım

country_code: Kod  
country_name: Ülke  
region: Bölge  
sub_region: Alt-Bölge  
year: Yıl  
month: Ay  
period: Tarih  
monthly_analyses: Aylık-Test  
cumulative_analyses: Toplam-Test  
unique_users: Kullanıcı  
repeat_user_rate: Sadakat  
avg_biomarkers_per_test: Parametre-Adedi
condition_healthy_pct: Sağlıklı  
condition_cardiovascular_pct: Kalp  
condition_diabetes_pct: Diyabet  
condition_metabolic_syndrome_pct: Metabolik  
condition_anemia_pct: Anemi  
condition_thyroid_pct: Tiroid  
condition_vitamin_d_deficiency_pct: Vit-D-Eksikliği  
condition_vitamin_b12_deficiency_pct: Vit-B12-Eksikliği  
condition_liver_pct: Karaciğer  
condition_kidney_pct: Böbrek  
condition_inflammation_pct: Enflamasyon  
risk_optimal_pct: İdeal   
risk_normal_pct: Normal  
risk_attention_pct: Dikkat  
risk_elevated_pct: Yüksek  
risk_critical_pct: Kritik  
avg_health_score: Sağlık-Puanı  
avg_cardiovascular_risk_score: Kalp-Skoru  
avg_metabolic_risk_score: Metabolik-Skor  
avg_nutrient_score: Besin-Skoru  
top_abnormal_biomarker_1: Bir-Hatalı  
top_abnormal_biomarker_2: İki-Hatalı  
top_abnormal_biomarker_3: Üç-Hatalı  
avg_biomarkers_out_of_range: Anomali-Adedi  
biomarker_abnormal_rate: Anomali-Oranı  


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

# global sağlık karnesi
<img width="1200" height="700" alt="global sağlık karnesi tüm zamanlar ort" src="https://github.com/user-attachments/assets/746af265-59bb-4b22-9873-14c2e6454e24" />
İtalya (73.26): Uzun vadede dünyanın en istikrarlı ve sağlıklı profili.  
Fransa (72.42): İkinci sırada sağlam bir yer edinmiş.  
Portekiz (72.39): Üçüncü olarak liderlik grubunda.
Brezilya (71.04): Genel ortalamada listenin sonunda yer alıyor.iyileştirme ihtiyacı olduğunu söyleyebiliriz

# Bölgelerin "Kronik" Sorunları
<img width="1200" height="700" alt="bölgeleregöre" src="https://github.com/user-attachments/assets/8c08659b-02fc-4022-8421-bcd4c1b12188" />
# bölgelere göre anemi 
<img width="1000" height="600" alt="bölgeleregöreanemi" src="https://github.com/user-attachments/assets/cd4a7578-47cc-4b30-a01b-8eda00c11cb6" />

Avrupa'nın En Büyük Sorunu: Vitamin D  
Kuzey Amerika'nın En Büyük Sorunu: LDL Kolesterol (kötü kolestrol) genellikle yüksek yağlı beslenme ve yaşam tarzıyla ilişkilendirilen bir durum.  
Güney Amerika'nın En Büyük Sorunu: Ferritin (Demir Deposu) Bir önceki analizdeki yüksek anemi oranını burada "Ferritin" (demir deposu) anomalisiyle doğrulamış oluyoruz. Güney Amerika için en büyük sağlık önerisi "demir takviyesi ve beslenme düzeni" olacaktır.

# Genel Performans Analizi (Tüm Zamanların Ortalaması)
<img width="1200" height="700" alt="global sağlık karnesi tüm zamanlar ort" src="https://github.com/user-attachments/assets/14577d18-3e28-487b-8350-f94badbe24d9" />

Zirvedekiler (Genel Ortalaması En Yüksek):İtalya (73.26): Uzun vadede dünyanın en istikrarlı ve sağlıklı profili.  
Fransa (72.42): İkinci sırada sağlam bir yer edinmiş.  
Portekiz (72.39): Üçüncü olarak liderlik grubunda.  
Kritik Bölgedekiler (Gelişime En Açık Olanlar):Brezilya (71.04): Genel ortalamada listenin sonunda yer alıyor. Brezilya'daki sorunun geçici olmadığını, kronik bir iyileştirme ihtiyacı olduğunu  söyleyebilirim.

# 
<img width="1536" height="762" alt="ortalamalarının bölgelerine göre karşılaştırılmasıgüncel" src="https://github.com/user-attachments/assets/d7c5a5f1-cf2f-4ae8-a619-1347903723fe" />
Analizimde mevsimsel dalgalanmaların etkisini azaltmak ve daha güvenilir bir karşılaştırma yapmak için son ay verisi yerine, her ülkenin tüm dönemlerdeki ortalama performansını bölge ortalamalarıyla kıyasladım

Sıfır Çizgisi: Bu çizgi o ülkenin bulunduğu bölgenin ortalamasını temsil ediyor.

Yeşil Çubuklar: Bölgesindeki diğer ülkelere göre ortalamayı yukarı çeken ülkeler.

Kırmızı Çubuklar: Bölge standartlarına göre sağlık skoru düşük kalan ve "neden?" diye sormamız gereken ülkeler.


# ülke sağlık segmentasyonu
<img width="1536" height="762" alt="ülke saglık segmentasyonu kümeleme analizi" src="https://github.com/user-attachments/assets/b10a0c2a-e3f2-4214-b856-958e22b7ae86" />
K-Means Kümeleme (Clustering) algoritma grupları oluştururken sadece görseldeki bu iki değişkeni değil, arka planda veri setindeki tüm sütunları (kardiyovasküler risk, yaşlı nüfus oranı vb.) kullanmıştır.  
United States (ABD), sağlık puanı nispeten yüksek olmasına rağmen diyabet yaygınlığında en tepede yer alarak gruptan ayrışıyor. Bu, ABD'nin sağlık sisteminin verimli ama beslenme/kronik hastalık yönetiminde sorunlu olduğunu gösterir.  
Yüksek Performans (Sarı X): İtalya ve Fransa düşük diyabet ile referans ülkelerdir.  
Risk Grubu (Kırmızı Daire): Brezilya ve ABD gibi ülkeler, diyabetle mücadele stratejilerinde müdahaleye ihtiyaç duyan "High-Risk" segmentindedir.  
Dengeli Grup (Yeşil Kare): Hollanda ve İspanya, sürdürülebilir bir sağlık modeline en yakın, stabil grubu temsil eder.  

# beslenme  planı etkisi
Puanımızı artırmak için nereye para harcamalıyız?  
<img width="1200" height="700" alt="beslenme işe yarıyo mu" src="https://github.com/user-attachments/assets/d1db8e0a-5ee1-47fa-863c-0b40b3402146" />
3 aylık bir "gecikme" (lag) koyarak, bugün atılan bir adımın (diyet planı), 3 ay sonraki kan tahlili sonuçlarına yansıyıp yansımadığını ölçtük.  
Korelasyon Düşük çıktı  <0.10   
Beslenme planı talebi ile 3 ay sonraki puanlar arasında doğrudan ve güçlü bir bağ saptanamadı. Bu durum, planların uygulanabilirliğinin düşük olduğunu veya iyileşme için 3 aydan daha uzun bir süreye ihtiyaç duyulduğunu gösteriyor olabilir.

# Engagement (Beslenme Planı) vs. İyileşme Hızı

<img width="1000" height="600" alt="beslenme talebi işe yarıyo mu güncel" src="https://github.com/user-attachments/assets/dfdf27e5-1f48-49ab-93d4-727739cb38c5" />
Kullanıcıların beslenme planı hizmetine olan ilgisi (Engagement), bir sonraki ayki sağlık skorlarında net bir iyileşme ile sonuçlanıyor. Bu, sunulan beslenme rehberliğinin sadece bir 'ek özellik' değil, sağlık çıktılarını doğrudan pozitif etkileyen bir kaldıraç olduğunu ispatlar.

