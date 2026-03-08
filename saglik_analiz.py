import pandas as pd
import sqlite3 # SQL veritabanı simülasyonu için
# 1. Önce SQL verisini Python'a tanıtalım
conn = sqlite3.connect(':memory:')
df_csv = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')
df_csv.to_sql('health_data', conn, index=False)

#SQL Sorgumuz
sql_sorgusu = """
SELECT 
    period,
    SUM(monthly_analyses) as total_tests,
    LAG(SUM(monthly_analyses)) OVER (ORDER BY period) as prev_month_tests
FROM health_data
GROUP BY period
"""

#SQL sonucunu doğrudan Python tablosuna (DataFrame) alıyoruz
df_buyume = pd.read_sql_query(sql_sorgusu, conn)
## Büyüme oranını Python tarafında hesaplayalım
df_buyume['growth_pct'] = ((df_buyume['total_tests'] - df_buyume['prev_month_tests']) / df_buyume['prev_month_tests']) * 100


#Çizgi Grafiği (Büyüme Analizi)
# --- BU KISMI SENİN KODUNLA DEĞİŞTİR ---

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax1 = plt.subplots(figsize=(14, 7))

# 1. Sol Eksen: Toplam Test Sayısı (Bar/Sütun Grafik olarak daha şık durur)
sns.barplot(data=df_buyume, x='period', y='total_tests', color='skyblue', alpha=0.6, ax=ax1)
ax1.set_ylabel('Toplam Test Sayısı', fontsize=12, color='blue')
ax1.set_title('Global Test Hacmi ve Aylık Büyüme Trendi', fontsize=16, fontweight='bold')
plt.xticks(rotation=45)

# 2. Sağ Eksen: Büyüme Yüzdesi (Çizgi Grafik)
ax2 = ax1.twinx() # İşte sihirli komut: Aynı grafiğe ikinci bir Y ekseni açar
sns.lineplot(data=df_buyume, x=range(len(df_buyume)), y='growth_pct', color='red', marker='o', linewidth=2.5, ax=ax2)
ax2.set_ylabel('Aylık Büyüme Oranı (%)', fontsize=12, color='red')

# Sıfır çizgisini ekleyelim (Büyüme mi daralma mı görmek için)
ax2.axhline(0, color='black', linestyle='--', linewidth=1)

plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
#figür1 test sayı değişimi


#Isı Haritası (Yaş ve Risk İlişkisi) güncellenmiş

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Veriyi Yükle
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')

# 2. Analiz Edilecek Sütun Gruplarını Tanımla
age_cols = ['age_18_29_pct', 'age_30_44_pct', 'age_45_59_pct', 'age_60_plus_pct']
health_cols = [
    'condition_cardiovascular_pct', 
    'condition_diabetes_pct', 
    'condition_metabolic_syndrome_pct', 
    'condition_anemia_pct', 
    'avg_health_score'
]

# 3. SENIOR DOKUNUŞU: Ülke Bazında Gruplama (Aggregation)
# Aylık dalgalanmaları temizlemek için her ülkenin genel ortalamasını alıyoruz
country_agg = df.groupby('country_name')[age_cols + health_cols].mean()

# 4. Korelasyon Matrisini Hesapla
# Sadece yaş grupları ile sağlık durumları arasındaki ilişkiye odaklanıyoruz
agg_corr = country_agg.corr().loc[age_cols, health_cols]

# 5. Görselleştirme
plt.figure(figsize=(12, 8))

# RdYlGn (Kırmızı-Sarı-Yeşil) paleti ile anlamlı bir ısı haritası
sns.heatmap(agg_corr, 
            annot=True,          # Sayıları üzerine yaz
            cmap='RdYlGn',       # Pozitifler yeşil, negatifler kırmızı
            center=0,            # 0 noktasını merkeze al (beyaz/sarı)
            fmt=".2f",           # Virgülden sonra 2 basamak
            linewidths=0.5,      # Kutular arasına ince çizgi
            cbar_kws={"label": "Korelasyon Katsayısı"})

plt.title('Ülke Bazlı Stratejik Sağlık Analizi: Yaş Grupları vs. Riskler\n(Aggregated Insights)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Sağlık Durumu / Risk Faktörleri', fontsize=12)
plt.ylabel('Yaş Grupları (%)', fontsize=12)

plt.tight_layout()


#-----------------------------------------------------------------------------------------------------------------------
#ekleme
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veriyi yükle
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')

# 2. Bölgelere göre grupla ve Anemi oranlarının ortalamasını al
anemi_analizi = df.groupby('region')['condition_anemia_pct'].mean().sort_values(ascending=False).reset_index()

# 3. Görselleştirme
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Bar grafik çizimi
ax = sns.barplot(data=anemi_analizi, x='region', y='condition_anemia_pct', palette='OrRd_r')

# Çubukların üzerine tam oranları yazalım (Senin sorduğun rakamlar burada görünecek)
for i, p in enumerate(ax.patches):
    ax.annotate(f'%{p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points', 
                fontweight='bold', fontsize=12)

plt.title('Bölgelere Göre Anemi (Kansızlık) Yaygınlığı Oranı', fontsize=15, fontweight='bold', pad=20)
plt.ylabel('Ortalama Anemi Oranı (%)', fontsize=12)
plt.xlabel('Bölge', fontsize=12)
plt.ylim(0, 40) # Farkın net görülmesi için üst sınırı 40 yapalım

plt.tight_layout()
#-----------------------------------------------------------------------------------------------------------------------------------------



#Bölgesel Sağlık Karnesi - bölgeleri gruplayıp ortalama sağlık puanlarını hesaplamak.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi oku
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')

# Bölgelere göre grupla ve ortalama sağlık puanını hesapla
bolgesel_skor = df.groupby('region')['avg_health_score'].mean().sort_values(ascending=False).reset_index()

# Görselleştirme
plt.figure(figsize=(10, 6))
sns.barplot(data=bolgesel_skor, x='region', y='avg_health_score', palette='magma')

# Grafik üzerine değerleri eklemek (Profesyonel bir dokunuş)
for i, skor in enumerate(bolgesel_skor['avg_health_score']):
    plt.text(i, skor + 1, f'{skor:.2f}', ha='center', fontweight='bold')

plt.title('Bölgelere Göre Ortalama Sağlık Puanı', fontsize=14)
plt.ylabel('Ortalama Puan')
plt.ylim(0, 100) # Skorlar 100 üzerindense ekseni sabitlemek iyidir




#Burada her bölgede en çok hangi biyomarker'ın sorunlu olduğunu buluyoruz.
# Her bölge ve o bölgedeki en sık görülen 1. anomaliyi sayalım
biyomarker_analiz = df.groupby(['region', 'top_abnormal_biomarker_1']).size().reset_index(name='count')

# En çok görülenleri yukarıda göstermek için sıralayalım
biyomarker_analiz = biyomarker_analiz.sort_values(['region', 'count'], ascending=[True, False])

# Görselleştirme
plt.figure(figsize=(12, 7))
sns.barplot(data=biyomarker_analiz, x='count', y='top_abnormal_biomarker_1', hue='region')

plt.title('Bölgelere Göre En Sık Rastlanan Anormal Biyomarkerlar', fontsize=14)
plt.xlabel('Görülme Sıklığı (Kayıt Sayısı)')
plt.ylabel('Biyomarker Tipi')
plt.legend(title='Bölge', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()







#Bölgesel Ortalamadan Sapma Analizi (benchmarking)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veriyi yükle
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')

# 2. Sadece son ayın verisini alalım (SQL'deki WHERE period = '2025-12' gibi)
latest_data = df[df['period'] == '2025-12'].copy()

# 3. Her bölgenin kendi ortalamasını hesaplayıp yeni bir sütun olarak ekleyelim
latest_data['regional_avg'] = latest_data.groupby('region')['avg_health_score'].transform('mean')

# 4. Farkı hesaplayalım (SQL'deki diff_from_avg)
latest_data['diff_from_avg'] = latest_data['avg_health_score'] - latest_data['regional_avg']

# 5. Görselleştirme için veriyi farka göre sıralayalım
latest_data = latest_data.sort_values('diff_from_avg')

# 6. Grafik Çizimi
plt.figure(figsize=(12, 8))

# Renkleri belirleyelim: Pozitifler Yeşil, Negatifler Kırmızı
colors = ['red' if x < 0 else 'green' for x in latest_data['diff_from_avg']]

plt.barh(latest_data['country_name'], latest_data['diff_from_avg'], color=colors)

# Grafik detayları
plt.axvline(0, color='black', linestyle='-', linewidth=1) # Sıfır çizgisi (Bölge Ortalaması)
plt.title('Ülkelerin Bölgesel Sağlık Ortalamasından Sapması (Benchmarking)', fontsize=15, fontweight='bold')
plt.xlabel('Ortalamadan Fark (Puan)', fontsize=12)
plt.ylabel('Ülke', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Not ekleyelim
plt.text(latest_data['diff_from_avg'].max(), len(latest_data)-1, ' Ortalamadan Daha Sağlıklı', color='green', fontweight='bold')
plt.text(latest_data['diff_from_avg'].min(), 0, ' Ortalamanın Altında ', color='red', fontweight='bold', ha='right')

plt.tight_layout()



# önceki plt ülkelerin sadece son ayı ile bölgeyi kıyaslıyordu şimdi ülkelerin ortalamasıyla bölgelerinin ortalamsını karşılaştıralım
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veriyi yükle
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')

# 2. Önce her ülkenin tüm zamanlardaki ortalama sağlık puanını hesaplayalım
country_perf = df.groupby(['country_name', 'region'])['avg_health_score'].mean().reset_index()

# 3. Şimdi her bölgenin kendi içindeki genel ortalamasını hesaplayalım
# Bu, her bölgedeki ülkelerin ortalamalarının ortalaması olacak
region_perf = country_perf.groupby('region')['avg_health_score'].transform('mean')
country_perf['regional_avg'] = region_perf

# 4. Genel farkı hesaplayalım (SQL'deki diff_from_avg mantığı ama tüm zamanlar için)
country_perf['diff_from_avg'] = country_perf['avg_health_score'] - country_perf['regional_avg']

# 5. Görselleştirme için sıralama
country_perf = country_perf.sort_values('diff_from_avg')

# 6. Grafik Çizimi
plt.figure(figsize=(12, 10))
colors = ['#e74c3c' if x < 0 else '#2ecc71' for x in country_perf['diff_from_avg']]

plt.barh(country_perf['country_name'], country_perf['diff_from_avg'], color=colors)

# Grafik detayları
plt.axvline(0, color='black', linestyle='-', linewidth=1.5)
plt.title('Ülkelerin Genel Sağlık Performansı: Bölgesel Ortalamadan Sapma\n(Tüm Zamanların Ortalaması)', fontsize=16, fontweight='bold')
plt.xlabel('Bölge Ortalamasından Fark (Puan)', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Dinamik etiketler ekleyelim
for i, v in enumerate(country_perf['diff_from_avg']):
    plt.text(v, i, f' {v:.2f}', va='center', fontweight='bold', color='black')

plt.tight_layout()




#hangi ülkeler iyi durumda hangileri ilgi istiyor? 
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# 1. ADIM: SQL BAĞLANTISI VE TABLO OLUŞTURMA
# Veriyi yüklüyoruz
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')

# Bellek üzerinde geçici bir SQL veritabanı açıyoruz
conn = sqlite3.connect(':memory:')

# Veriyi senin istediğin isimle (saglik_analizleri) SQL'e kaydediyoruz
df.to_sql('saglik_analizleri', conn, index=False)

# 2. ADIM: SQL SORGUSU İLE VERİ ÇEKME
# Python içinde SQL gücünü kullanarak veriyi çekiyoruz (df_segments burada doğuyor)
sql_sorgusu = """
SELECT 
    country_name, 
    avg_health_score 
FROM saglik_analizleri 
WHERE period = '2025-12' 
ORDER BY avg_health_score DESC
"""
df_segments = pd.read_sql_query(sql_sorgusu, conn)

# 3. ADIM: GÖRSELLEŞTİRME (Top vs. Bottom)
# En yüksek 3 ve en düşük 3 ülkeyi seçiyoruz
top_bottom_df = df_segments.iloc[[0, 1, 2, -3, -2, -1]] 

plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")

# Renk paleti: Zirvedekiler yeşil tonları, diptekiler turuncu/kırmızı tonları
colors = ['#27ae60', '#2ecc71', '#a2d149', '#f39c12', '#e67e22', '#d35400']

# Bar grafik çizimi
ax = sns.barplot(data=top_bottom_df, x='avg_health_score', y='country_name', palette=colors)

# Şehir isimlerinin yanına puanlarını yazdıralım
for i, p in enumerate(ax.patches):
    ax.annotate(f'{p.get_width():.1f}', 
                (p.get_width(), p.get_y() + p.get_height() / 2.), 
                ha = 'left', va = 'center', 
                xytext = (7, 0), 
                textcoords = 'offset points', 
                fontweight='bold', fontsize=11)

# Grafik süslemeleri
plt.title('Global Sağlık Karnesi: Zirvedeki Şehirler ve Kritik Bölgedekiler\n(Aralık 2025 Verileri)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Ortalama Sağlık Puanı', fontsize=12)
plt.ylabel('Ülke / Şehir', fontsize=12)

# Farkı vurgulamak için ekseni 60'tan başlatalım
plt.xlim(60, 80) 

# Profesyonel görünüm için kenarlıkları sadeleştirelim
sns.despine(left=True, bottom=True)
plt.tight_layout()


# önceki kodda sadece aralık 2025 verileriyle yapılan bir karşılaştırma vardı şimdi Bu kod, saglik_analizleri tablosundaki tüm verileri tarar, ülkelerin genel ortalamasını hesaplar ve en iyi 3 ile en kötü 3'ü kıyaslar.

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# 1. SQL Bağlantısı
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('saglik_analizleri', conn, index=False)

# 2. SQL SORGUSU: Tüm zamanların ortalamasını alıyoruz (Daha sağlam analiz)
sql_sorgusu = """
SELECT 
    country_name, 
    ROUND(AVG(avg_health_score), 2) as avg_score_all_time
FROM saglik_analizleri 
GROUP BY country_name
ORDER BY avg_score_all_time DESC
"""
df_avg_segments = pd.read_sql_query(sql_sorgusu, conn)

# En iyi 3 ve en kötü 3'ü birleştirelim
top_bottom_avg = pd.concat([df_avg_segments.head(3), df_avg_segments.tail(3)])

# 3. Görselleştirme
plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")

# Profesyonel Renkler
colors = ['#27ae60', '#2ecc71', '#a2d149', '#f39c12', '#e67e22', '#d35400']

ax = sns.barplot(data=top_bottom_avg, x='avg_score_all_time', y='country_name', palette=colors)

# Puan Etiketlerini Ekle
for i, p in enumerate(ax.patches):
    ax.annotate(f'{p.get_width():.2f}', 
                (p.get_width(), p.get_y() + p.get_height() / 2.), 
                ha = 'left', va = 'center', 
                xytext = (7, 0), textcoords = 'offset points', 
                fontweight='bold', fontsize=11)

plt.title('Global Sağlık Karnesi: Genel Performans Zirvedekiler vs. Kritiktekiler\n(Tüm Zamanların Ortalaması)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Genel Ortalama Sağlık Puanı', fontsize=12)
plt.ylabel('Ülke / Şehir', fontsize=12)
plt.xlim(60, 80) 

plt.tight_layout()



#Analiz: Ülkeleri diyabet, kolesterol, yaş ortalaması ve sağlık puanlarına göre K-Means algoritmasıyla kümelemek.
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. VERİ HAZIRLIĞI VE SQL BAĞLANTISI
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')
conn = sqlite3.connect(':memory:')

# Tablo ismini senin istediğin gibi "saglik_analizleri" yapıyoruz
df.to_sql('saglik_analizleri', conn, index=False)

# 2. SQL İLE ÖZELLİK MÜHENDİSLİĞİ (Feature Engineering)
# Ülkelerin karakterini belirleyen 4 ana metriği SQL ile çekiyoruz
sql_sorgusu = """
SELECT 
    country_name,
    AVG(avg_health_score) as health_score,
    AVG(condition_diabetes_pct) as diabetes_pct,
    AVG(condition_cardiovascular_pct) as cardio_pct,
    AVG(age_60_plus_pct) as age_60plus_pct
FROM saglik_analizleri
GROUP BY country_name
"""
df_cluster = pd.read_sql_query(sql_sorgusu, conn)

# 3. MAKİNE ÖĞRENMESİ İÇİN VERİ ÖLÇEKLENDİRME
# K-Means mesafe ölçtüğü için tüm verileri (0-1) veya (-1 ile 1) arasına çekmeliyiz
features = ['health_score', 'diabetes_pct', 'cardio_pct', 'age_60plus_pct']
x = df_cluster[features]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# 4. K-MEANS ALGORİTMASININ ÇALIŞTIRILMASI
# Ülkeleri 3 ana kümeye ayırıyoruz
kmeans = KMeans(n_init=10, n_clusters=3, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(x_scaled)

# Küme numaralarını anlamlı isimlere çevirelim
cluster_map = {0: 'Risk Grubu', 1: 'Dengeli Grup', 2: 'Yüksek Performans'}
df_cluster['segment'] = df_cluster['cluster'].map(cluster_map)

# 5. GÖRSELLEŞTİRME (Scatter Plot)
plt.figure(figsize=(14, 8))
sns.set_style("white")

# Diyabet vs Sağlık Puanı ekseninde kümeleri görelim
ax = sns.scatterplot(data=df_cluster, x='health_score', y='diabetes_pct', 
                hue='segment', style='segment', s=300, 
                palette=['#e74c3c', '#f1c40f', '#2ecc71'], alpha=0.8)

# Ülke isimlerini noktaların üzerine ekleyelim (Analist dokunuşu)
for i in range(df_cluster.shape[0]):
    plt.text(df_cluster.health_score[i]+0.05, df_cluster.diabetes_pct[i]+0.2, 
             df_cluster.country_name[i], fontsize=10, fontweight='semibold')

plt.title('Ülke Sağlık Segmentasyonu: K-Means Kümeleme Analizi', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Ortalama Sağlık Puanı', fontsize=12)
plt.ylabel('Diyabet Yaygınlığı (%)', fontsize=12)
plt.legend(title='Sağlık Segmenti', bbox_to_anchor=(1, 1))
plt.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()

# 6. KIDEMLİ ANALİST ÖZETİ (Konsol Çıktısı)
print("\n--- SEGMENTASYON ÖZETİ ---")
print(df_cluster.groupby('segment')[features].mean())



import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# 1. SQL Bağlantısı (Daha önce kurduysan bu kısmı atlayabilirsin)
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('saglik_analizleri', conn, index=False)

# 2. SQL: LEAD Fonksiyonu ile Geleceği Getirme
# Her satıra, aynı ülkenin 3 ay sonraki sağlık puanını (LEAD) ekliyoruz.
sql_lagged = """
SELECT 
    country_name,
    period,
    nutrition_plan_requested_pct,
    LEAD(avg_health_score, 3) OVER (PARTITION BY country_name ORDER BY period) as health_score_3m_later
FROM saglik_analizleri
"""
df_lagged = pd.read_sql_query(sql_lagged, conn)

# Gelecek verisi olmayan son ayları temizleyelim (NaN değerleri)
df_lagged_clean = df_lagged.dropna(subset=['health_score_3m_later'])

# 3. Görselleştirme (Regresyon Grafiği)
plt.figure(figsize=(12, 7))
sns.regplot(data=df_lagged_clean, x='nutrition_plan_requested_pct', y='health_score_3m_later', 
            scatter_kws={'alpha':0.5, 'color':'teal'}, line_kws={'color':'red', 'label':'Eğilim Çizgisi'})

# Korelasyon katsayısını hesaplayalım
corr_val = df_lagged_clean['nutrition_plan_requested_pct'].corr(df_lagged_clean['health_score_3m_later'])

plt.title(f'Stratejik Analiz: Beslenme Planı Etkisi (3 Ay Gecikmeli)\nKorelasyon: {corr_val:.2f}', fontsize=15, fontweight='bold')
plt.xlabel('Beslenme Planı Talep Oranı (%)', fontsize=12)
plt.ylabel('3 Ay Sonraki Sağlık Puanı', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

#Beslenme planı talebi ile 3 ay sonraki puanlar arasında doğrudan ve güçlü bir bağ saptanamadı. Bu durum, planların uygulanabilirliğinin düşük olduğunu veya iyileşme için 3 aydan daha uzun bir süreye ihtiyaç duyulduğunu gösteriyor olabilir.






#-----------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Veri Hazırlığı
df = pd.read_csv('kantesti_global_health_insights_2025_2026.csv')
df = df.sort_values(by=['country_name', 'period'])

# 2. İyileşme Hızını (Delta) Hesaplama
# Önemli: Mevcut aydaki etkileşimin, bir sonraki ayki sağlık puanını nasıl değiştirdiğine bakıyoruz.
df['next_month_health_score'] = df.groupby('country_name')['avg_health_score'].shift(-1)
df['delta_health_score'] = df['next_month_health_score'] - df['avg_health_score']

# 3. Etkileşim (Engagement) Gruplarını Belirleme
# Beslenme planı talebi medyan değerin üstünde olanlar "Yüksek Talep", altında olanlar "Düşük Talep"
median_nutrition = df['nutrition_plan_requested_pct'].median()
df['nutrition_group'] = np.where(df['nutrition_plan_requested_pct'] > median_nutrition, 'Yüksek Talep', 'Düşük Talep')

# 4. Görselleştirme (Boxplot)
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Analiz: Beslenme planı talebi ile bir sonraki ay gerçekleşen sağlık puanı değişimi (Delta)
ax = sns.boxplot(data=df.dropna(subset=['delta_health_score']), 
                x='nutrition_group', y='delta_health_score', 
                palette='Set2', showmeans=True,
                meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"10"})

plt.title('Engagement Analizi: Beslenme Planı Talebi vs. İyileşme Hızı (Delta)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Beslenme Planı Talep Segmenti', fontsize=12)
plt.ylabel('Bir Sonraki Ay Sağlık Puanı Değişimi (Delta)', fontsize=12)

# Analiz notu ekleyelim
plt.figtext(0.5, -0.05, "Not: Pozitif Delta, sağlık puanının bir sonraki ay yükseldiğini; negatif Delta ise düştüğünü gösterir.", 
            ha="center", fontsize=10, style='italic')

plt.tight_layout()
plt.show()

# 5. İstatistiksel Sonuçları Yazdır
summary = df.dropna(subset=['delta_health_score']).groupby('nutrition_group')['delta_health_score'].mean()
print(f"--- Gruplara Göre Ortalama İyileşme (Delta) ---")
print(summary)