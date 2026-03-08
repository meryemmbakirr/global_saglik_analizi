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



