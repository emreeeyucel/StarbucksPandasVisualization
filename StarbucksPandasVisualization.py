import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(filepath_or_buffer='data/starbucks.csv', encoding='utf-8')
print(df.head().to_string())

# region Veri İncelemesi

print(df.shape)
print(df.info())
# endregion



# region Eksik Değer Kontrolü

print(df.isna().sum())
# endregion



# region Veri Detayları

df.drop(labels='Unnamed: 0', axis=1, inplace=True)
print(df.head().to_string())
print(df.describe().T)
# endregion



# region Çeşitli "type" kategorilerindeki ürünlerin ortalama kalorilerini karşılaştıran bir "line" grafiği

type_mean = df.groupby('type')['calories'].mean().reset_index()
type_mean.plot(kind='line', x='type', y='calories', marker='s', color='green')
plt.title('Ürün Tiplerine Göre Ortalama Kalori Dağılımı', color='red', fontsize=16, loc='center')
plt.ylabel('Değerler', color='red')
plt.xlabel('Ürün Çeşitleri', color='red')
plt.grid(True, alpha=0.6, linestyle=':')
plt.savefig('Ürün Tiplerine Göre Ortalama Kalori Dağılımı.png')
plt.show()
# endregion



# region Ürünleri calories ve carb verilerine göre karşılaştıran "bar" grafiği

df.plot(kind='bar', x='item', y=['calories', 'carb'], color=['blue', 'red'], edgecolor='black')
plt.title('Ürünlerin Kalori ve Karbonhidrat İçerikleri', color='red', fontsize=16, loc='left')
plt.ylabel('Değerler', color='red')
plt.xlabel('Ürünler', color='red')
plt.grid(True, alpha=0.3, linestyle='-')
plt.subplots_adjust(top=1, bottom=0.15, left=0.1, right=0.9)  # Sırasıyla üst boşluğu, alt boşluğu sol ve sağ boşlukları hizalar.
plt.tight_layout()
plt.savefig('Ürünlerin Kalori ve Karbonhidrat İçerikleri.png')
plt.show()
# endregion



# region Besin değerlerinin "box" grafiği incelemesi.

df.plot(kind='box', y=['fat', 'protein', 'fiber', 'calories'], subplots=True, grid=True)
plt.suptitle('Besin Değerlerinin Dağılım Analizi', color='red', fontsize=15)                    # subplots oluşturulduğunda tüm subplotları kapsayan bir başlık eklemek için kullanılır.
plt.show()
# endregion



# region Type Kategorilerinin Yüzdelik Gösterimi(Pie Grafiği)

colors = ['lightblue', 'lightgreen', 'orange', 'pink']
df.groupby('type')['item'].count().plot(kind='pie', y='count', autopct="%1.1f%%", color=colors, startangle=90)
plt.title('Ürün Tiplerine Göre Yüzdelik Dağılım', fontsize=14, color='blue')
plt.ylabel('')
plt.tight_layout()
plt.savefig('Ürün Tiplerine Göre Yüzdelik Dağılım.png')
plt.show()
# endregion



# region Fırın Ürünlerinde Yağ ve Karbonhidrat Arasındaki İlişkiyi Gösteren "Scatter" Grafiği

df_bakery = df[df['type'] == 'bakery'][['type', 'fat', 'carb']]
df_bakery.plot(kind='scatter', x='fat', y='carb', color='green')
plt.title('Yağ ve Karbonhidrat İlişkisi', color='red', fontsize=16, loc='center')
plt.grid(True, alpha=0.3, linestyle='-')
plt.savefig('Yağ ve Karbonhidrat İlişkisi.png')
plt.show()
# endregion



# region Fiber Değerlerinin Histogram Grafiği

df.plot(kind='hist', y='fiber', color='skyblue', edgecolor='black', bins=50)
plt.title('Fiber Değerlerinin Sıklık Değerleri', color='red')
plt.ylabel('Tekrar Sıklığı', color='red')
plt.yticks(ticks=range(0, int(df['fiber'].value_counts().max() +1)))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig('Fiber Sıklık Bilgisi.png')
plt.show()
# endregion



# region Protein Dağılımı - KDE

df.plot(kind='kde', y='protein', color='purple', linestyle='--')
plt.title('Protein Dağılımı - KDE', fontsize=16)
plt.xlabel('Protein Miktarı', fontsize=12)
plt.ylabel('Yoğunluk', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
# endregion



# region Area Grafiği: fiber ve protein İçeriği

df.plot(kind='area', y=['fiber', 'protein'], x='item', alpha=0.6, color=['lightblue', 'lightgreen'])
plt.xticks(ticks=range(len(df['item'])), labels=df['item'], rotation=90)
plt.title('Fiber ve Protein Miktarları', fontsize=18, fontweight='bold', color='navy')
plt.xlabel('Ürünler', fontsize=14, color='darkgreen')
plt.ylabel('Miktar (g)', fontsize=14, color='darkgreen')
plt.ylim(0, df[['fiber', 'protein']].max().max() + 10)
plt.grid(True, linestyle='--', color='gray', alpha=0.5)
plt.legend(title='Bileşenler', loc='upper left')
plt.tight_layout()
plt.show()
# endregion



# region Her kategori (type) için kalori değerlerinin ortalama, toplam, maksimum ve minimum değerlerini hesaplayarak bar grafiği oluşturun.

type_calories_mean = df.groupby('type')[['calories']].agg(['mean', 'sum', 'max', 'min'])
type_calories_mean.plot(kind='bar', title='Kalori Değerleri', edgecolor='black')
plt.ylabel('Değerler', color='red')
plt.xlabel('Ürün Çeşit', color='red')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(title='Grafik Açıklamaları')
plt.tight_layout()
plt.show()
# endregion



# region Her kategori (type) için "agg" fonksiyonu kullanarak kalori değerlerinin toplam ve maksimum bar grafiği oluşturun.

df.groupby('type')[['calories']].agg(['mean', 'sum', 'max']).reset_index().plot(kind='bar', x='type', y=[('calories', 'sum'), ('calories', 'max')])
plt.ylabel('Değerler', color='red')
plt.xlabel('Ürün Çeşit', color='red')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(title='Grafik Açıklamaları')
plt.tight_layout()
plt.show()

# Burada, agg fonksiyonu sonucu oluşturulan çok seviyeli sütun adlarını kullanıyoruz eksenlere yerleştirken uygun yerleştirmemiz gerekmektedir.Eğer Tüm sütunları grafikte gösterceksek eksende belirtmemize gerek yok indexler x, sütunlar y ekseninde varlığını sürdürür. Bir üst örneğimizden farkı gösterir bu durumda.
# endregion



# region Ürün Türüne Göre Toplam Yağ Miktarını Gösterin

df.groupby('type')['fat'].sum().plot(kind='pie', figsize=(8,8), autopct='%1.1f%%', startangle=90,wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}, textprops={'color': 'black', 'fontsize': 12})
plt.title('Ürün Türüne Göre Toplam Yağ Miktarı')
plt.tight_layout()
plt.show()
# endregion



# region Yağ ile Kalori Arasındaki İlişkiyi Gösterin

df.plot(kind='scatter', x='fat', y='calories', figsize=(8, 6), color='purple')
plt.title('Yağ ile Kalori Arasındaki İlişki')
plt.xlabel('Yağ')
plt.ylabel('Kalori')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
# endregion


# region Protein İçeren Ürünleri Gösterin

df[df['protein'] > 0].plot(kind='barh', x='item', y='protein', figsize=(10, 6), color='lightgreen')
plt.title('Protein İçeren Ürünler')
plt.xlabel('Protein (gram)')
plt.ylabel('Ürünler')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(title='Grafik Açıklamaları')
plt.show()
# endregion


# region Toplam Protein Değeri 10 ile 15 Arasındaki Ürünleri Gösterin

df[df['protein'].between(10, 15)].plot(kind='bar', x='item', y='protein')
plt.title('10-15 gr Protein İçeren Ürünler')
plt.xlabel('Protein (gram)')
plt.ylabel('Ürünler')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(title='Grafik Açıklamaları')
plt.show()
# endregion


# region Toplam Protein Değeri 5 ile 15 Arasındaki ve Kalori Değeri 300 aşağısnda olan ürünleri Bar ile Gösterelim.

ax = df[(df['protein'].between(5, 15)) & (df['calories'] < 300)].plot(
    kind='bar',
    x='item',
    y=['calories', 'protein'],
    figsize=(10, 6),
    color=['skyblue', 'orange']
)
ax.set_title('Protein ve Kalori Değerleri (5-15 Protein, 0 - 300 Arası Kalori)', fontsize=14)
ax.set_xlabel('Ürünler', fontsize=12)
ax.set_ylabel('Değerler', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Besin Bilgisi', fontsize=10)
plt.tight_layout()
plt.show()
# endregion



# region En Yüksek Kaloriye Sahip 10 Ürünü Gösterin

top_10 = df.nlargest(10, 'calories', keep='all')
ax = top_10.plot(kind='barh', x='item', y='calories', figsize=(12, 7), color=plt.cm.viridis(top_10['calories'] / top_10['calories'].max()))
ax.set_title('En Yüksek Kaloriye Sahip 10 Ürün', fontsize=16, fontweight='bold', color='darkblue')
ax.set_xlabel('Kalori', fontsize=14, fontweight='bold', color='darkgreen')
ax.set_ylabel('Ürünler', fontsize=14, fontweight='bold', color='darkgreen')
ax.tick_params(axis='y', labelsize=12)                         #  axis = hangi eksen olduğu, eksendeki etiketlerin yazı tipi boyutunu büyütür veya küçültür.Y eksenindeki etiketlerin yazı boyutunu 12 yap
ax.tick_params(axis='x', labelsize=12)
plt.xticks(rotation=0, fontweight='light', fontsize=12)
plt.yticks(fontweight='light', fontsize=12)
plt.gca().set_facecolor("lightgray")  # Grafik alanının arka planı
plt.gcf().set_facecolor("lightblue")  # Dış alanın arka planı

# Bar kenarlıklarını koyulaştır
for bar in ax.patches:
    bar.set_edgecolor('black')
    bar.set_linewidth(1.5)
plt.show()
# endregion



# region En Düşük Kaloriye Sahip 10 Ürünü Gösterin

top_10_low = df.nsmallest(10, 'calories')
colors = plt.cm.plasma(top_10_low['calories'] / top_10_low['calories'].max())
ax = top_10_low.plot(kind='bar', x='item', y='calories', figsize=(12, 7), color=colors, edgecolor='black')
ax.set_title('En Düşük Kaloriye Sahip 10 Ürün', fontsize=16, fontweight='bold', color='darkblue')
ax.set_xlabel('Ürünler', fontsize=14, fontweight='bold', color='darkgreen')
ax.set_ylabel('Kalori', fontsize=14, fontweight='bold', color='darkgreen')
plt.gca().set_facecolor("lightgray")
plt.gcf().set_facecolor("lightblue")

# Etiket boyutlarını ayarlama
ax.tick_params(axis='x', labelsize=12, rotation=45, labelcolor='black')
ax.tick_params(axis='y', labelsize=12, labelcolor='black')

plt.tight_layout()
plt.show()
# endregion



# region Ürün Türlerine Göre Ortalama Protein Değeri Nasıldır

protein_means = df.groupby('type')['protein'].mean()
colors = plt.cm.magma(protein_means / protein_means.max())
fig, ax = plt.subplots(figsize=(12, 7))
protein_means.plot(kind='bar', color=colors, edgecolor='black', ax=ax)
ax.set_title('Ürün Türlerine Göre Ortalama Protein Değeri', fontsize=18, fontweight='bold', color='darkblue')
ax.set_xlabel('Ürün Türü', fontsize=14, fontweight='bold', color='darkgreen')
ax.set_ylabel('Ortalama Protein (gram)', fontsize=14, fontweight='bold', color='darkgreen')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_facecolor("beige")  # Grafik alanının arka planı
fig.patch.set_facecolor("lightblue")  # Dış alanın arka planı


# Değer etiketlerini ekleme
for i, value in enumerate(protein_means):
    ax.text(i, value +1, f'{value:.1f}', ha='center', va='bottom', fontsize=12, fontweight='bold', color='darkred')


# X ve Y eksen ayarları
ax.tick_params(axis='x', labelsize=12, labelcolor='black')
ax.tick_params(axis='y', labelsize=12, labelcolor='black')


# Kenarlıkları ayarlama
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.tight_layout()
plt.show()
# endregion



# region Karbonhidrat Miktarı ile Kalori Arasındaki İlişkiyi Gösterin

df.plot(kind='scatter', x='carb', y='calories', figsize=(8, 6), color='orange')
plt.title('Karbonhidrat Miktarı ile Kalori Arasındaki İlişki')
plt.xlabel('Karbonhidrat (gr)')
plt.ylabel('Kalori')
plt.show()
# endregion


# region Ürünlerin Kalori Miktarını Dağılım Grafiği ile Gösterin

df['calories'].plot(kind='hist', bins=20, figsize=(8,6), color='green', edgecolor='black')
plt.title('Ürünlerin Kalori Dağılımı')
plt.xlabel('Kalori')
plt.ylabel('Frekans')
plt.tight_layout()
plt.show()
# endregion


# region Yağ ve Karbonhidrat Arasındaki İlişkiyi Gösterin

df.plot(kind='scatter', x='fat', y='carb', figsize=(8, 6), color='red')
plt.title('Yağ ve Karbonhidrat Arasındaki İlişki')
plt.xlabel('Yağ (gram)')
plt.ylabel('Karbonhidrat(gr)')
plt.show()
# endregion



# region Ürünlerin Kalori Miktarını Dağılım Grafiği ile Gösterin

df['calories'].plot(kind='hist', bins=20, figsize=(8,6), color='green', edgecolor='black')
plt.title('Ürünlerin Kalori Dağılımı')
plt.xlabel('Kalori')
plt.ylabel('Frekans')
plt.tight_layout()
plt.show()
# endregion



# region Korelasyon Heatmap — “Besin Değerleri Arasındaki İlişki”


plt.style.use('seaborn-v0_8-whitegrid')

numeric_cols = ['calories', 'fat', 'carb', 'protein', 'fiber']
corr = df[numeric_cols].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='Greens', fmt=".2f", linewidths=1, cbar_kws={'label': 'Korelasyon Değeri'})
plt.title(' Besin Değerleri Arasındaki Korelasyon', fontsize=16, fontweight='bold', color='#00704A', pad=20)
plt.tight_layout()
plt.show()

# Kalori ile yağ arasında güçlü pozitif korelasyon, protein ile kalori arasında orta düzey ilişki beklenir.
# endregion



# region Protein ve Kalori Yoğunluğu Dağılımı — “Sağlık Skoru Analizi

df['protein_efficiency'] = df['protein'] / df['calories']
df['density'] = df['calories'] / (df['protein'] + df['carb'] + df['fat'])

fig, ax = plt.subplots(figsize=(10,6))
scatter = ax.scatter(df['density'], df['protein_efficiency'],
                     c=df['calories'], cmap='Greens', s=120, edgecolor='black', alpha=0.8)

ax.set_title('💚 Protein ve Kalori Yoğunluğu Dağılımı', fontsize=18, fontweight='bold', color='#00704A')
ax.set_xlabel('Kalori Yoğunluğu (Cal / (Protein + Carb + Fat))', fontsize=12, color='#4B2E05')
ax.set_ylabel('Protein Verimliliği (Protein / Calorie)', fontsize=12, color='#4B2E05')
ax.grid(True, linestyle='--', alpha=0.5)
cbar = plt.colorbar(scatter)
cbar.set_label('Kalori Düzeyi', fontsize=11, color='#004D40', fontweight='bold')
plt.tight_layout()

plt.show()

# endregion



# region Kategori Bazlı Ortalama Besin Değerleri
type_means = df.groupby('type')[['calories', 'fat', 'carb', 'protein', 'fiber']].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,6))
type_means.set_index('type').plot(kind='bar', ax=ax, colormap='Greens', edgecolor='black')

ax.set_title('Kategori Bazlı Ortalama Besin Değerleri', fontsize=18, fontweight='bold', color='#00704A')
ax.set_xlabel('Ürün Türü', fontsize=12, color='#4B2E05')
ax.set_ylabel('Ortalama Değer', fontsize=12, color='#4B2E05')
ax.legend(title='Besin Türü', loc='upper right', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
# endregion



# region 10–15g Protein Arası Ürünlerin Karşılaştırması — “Orta Protein Grubu
mid_protein = df[df['protein'].between(10, 15)]

fig, ax = plt.subplots(figsize=(12,6))
bars = ax.bar(mid_protein['item'], mid_protein['protein'], color=cm.Greens(np.linspace(0.4, 1, len(mid_protein))), edgecolor='black')

ax.set_title('🌿 10–15g Protein İçeren Ürünlerin Karşılaştırması', fontsize=18, fontweight='bold', color='#00704A', pad=20)
ax.set_xlabel('Ürünler', fontsize=12, color='#4B2E05')
ax.set_ylabel('Protein (gram)', fontsize=12, color='#4B2E05')
ax.set_facecolor('#E8F5E9')
fig.patch.set_facecolor('#F5F1E7')
plt.xticks(rotation=45, ha='right')

# Değer etiketleri ekleyelim
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.3, f'{height:.1f}', ha='center', fontsize=10, fontweight='bold', color='#1B5E20')

plt.tight_layout()
plt.show()
# endregion



# region Kategori Bazlı Sağlık Skoru
df['health_score'] = (df['protein'] - df['fat']) / df['calories']
type_health = df.groupby('type')['health_score'].mean().sort_values(ascending=False)
type_health.plot(kind='bar', color='green', edgecolor='black')
plt.title('Ürün Tiplerine Göre Ortalama Sağlık Skoru')
plt.show()
# endregion



# region En Yüksek Kalorili 5 Ürünün Besin Dağılımı

top5 = df.nlargest(5, 'calories')[['item', 'fat', 'carb', 'protein']]
top5.set_index('item', inplace=True)

top5.plot(kind='bar', stacked=True, figsize=(10,6),
          color=['#CBB26A', '#A7E3A1', '#006241'], edgecolor='#4B2E05', linewidth=1.5)

plt.title('En Yüksek Kalorili 5 Ürünün Besin Bileşimi', fontsize=16, fontweight='bold', color='#006241')
plt.xlabel('Ürünler', fontsize=12, color='#4B2E05')
plt.ylabel('Miktar (gram)', fontsize=12, color='#4B2E05')
plt.legend(title='Bileşenler', loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.6, color='#CBB26A')
plt.gca().set_facecolor('#F5F1E7')
plt.tight_layout()
plt.show()
# endregion



# region Fiber ve Protein Oranı — Sağlık Dengesi Analizi

avg_values = df.groupby('type')[['fiber', 'protein']].mean()

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(avg_values.index, avg_values['fiber'], label='Fiber', color='#A7E3A1', edgecolor='#006241', linewidth=1.5)
ax.bar(avg_values.index, avg_values['protein'], bottom=avg_values['fiber'],
       label='Protein', color='#006241', edgecolor='#006241', linewidth=1.5)

ax.set_title('Kategori Bazlı Ortalama Fiber ve Protein Miktarı', fontsize=16, color='#006241', fontweight='bold')
ax.set_xlabel('Ürün Tipi', fontsize=12, color='#4B2E05')
ax.set_ylabel('Ortalama Miktar (gram)', fontsize=12, color='#4B2E05')
ax.legend(facecolor='#F5F1E7', edgecolor='#4B2E05')
ax.set_facecolor('#F5F1E7')
ax.grid(axis='y', linestyle='--', alpha=0.5, color='#A7E3A1')
plt.tight_layout()
plt.show()
# endregion



# region Kaloriye Göre Protein/Yağ Oranı — Enerji Dengesi

df['ratio_protein_fat'] = df['protein'] / (df['fat'] + 1)

plt.figure(figsize=(10,6))
plt.scatter(df['calories'], df['ratio_protein_fat'],
            c=df['protein'], cmap='cool', s=120, edgecolor='#4B2E05', alpha=0.85)

plt.title('Kaloriye Göre Protein/Yağ Oranı Dağılımı', fontsize=16, fontweight='bold', color='#2F4F4F')
plt.xlabel('Kalori', fontsize=12, color='#2F4F4F')
plt.ylabel('Protein / Yağ Oranı', fontsize=12, color='#2F4F4F')
plt.grid(True, linestyle='--', alpha=0.4, color='#B0C4DE')
plt.colorbar(label='Protein (g)')
plt.gca().set_facecolor('#F0F8FF')
plt.tight_layout()
plt.show()
# endregion



# region Aykırı Değer Analizi — Kalori

q1 = df['calories'].quantile(0.25)
q3 = df['calories'].quantile(0.75)
iqr = q3 - q1
outliers = df[df['calories'] > q3 + 1.5 * iqr]

plt.figure(figsize=(10,6))
plt.boxplot(df['calories'], patch_artist=True,
            boxprops=dict(facecolor='#E0E0E0', color='#4B2E05', linewidth=1.5),
            medianprops=dict(color='#C0392B', linewidth=2))

plt.scatter([1]*len(outliers), outliers['calories'], color='#C0392B', label='Aykırı Ürünler', zorder=3, s=80, edgecolor='#4B2E05')
plt.title('Aykırı Kalori Değerleri (Outlier Analizi)', fontsize=16, fontweight='bold', color='#4B2E05')
plt.ylabel('Kalori', fontsize=12, color='#4B2E05')
plt.legend(facecolor='#F5F1E7', edgecolor='#4B2E05')
plt.gca().set_facecolor('#F5F1E7')
plt.grid(axis='y', linestyle='--', alpha=0.4, color='#D0D0D0')
plt.tight_layout()
plt.show()

print("Aykırı Kalorili Ürünler:")
print(outliers[['item', 'type', 'calories']])
# endregion



# region Geliştirilmiş Boxplot - Kategori Bazlı Kalori Dağılımı

plt.figure(figsize=(10,6))
ax = plt.gca()
ax.set_facecolor('#F5F1E7')  # Krem arka plan

# Boxplot
box = df.boxplot(column='calories', by='type', grid=False, ax=ax,
           boxprops=dict(color='#006241', linewidth=1.5, facecolor='#A7E3A1'),
           whiskerprops=dict(color='#006241', linewidth=1.5),
           capprops=dict(color='#006241', linewidth=1.5),
           medianprops=dict(color='#CBB26A', linewidth=2.5),
           flierprops=dict(marker='o', color='#C0392B', alpha=0.7, markersize=6),
           patch_artist=True)

# Başlık ve eksenler
plt.title('Kategori Bazlı Kalori Dağılımı', fontsize=16, fontweight='bold', color='#006241')
plt.suptitle('')
plt.xlabel('Ürün Tipi', fontsize=12, color='#4B2E05')
plt.ylabel('Kalori', fontsize=12, color='#4B2E05')

# Grid & çizgiler
plt.grid(axis='y', linestyle='--', alpha=0.4, color='#CBB26A')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Küçük aralıklar ve düzen
plt.xticks(rotation=15, color='#4B2E05')
plt.yticks(color='#4B2E05')
plt.tight_layout()
plt.show()

# endregion



# region Kalori - Protein İlişkisi (Scatter)
plt.figure(figsize=(10,6))
plt.scatter(df['calories'], df['protein'],
            color='red', edgecolor='black', alpha=0.7)

plt.title('Kalori ve Protein Arasındaki İlişki', fontsize=16, color='#1B4F72', fontweight='bold')
plt.xlabel('Kalori', fontsize=12, color='#1B2631')
plt.ylabel('Protein (g)', fontsize=12, color='#1B2631')
plt.grid(True, linestyle='--', alpha=0.4, color='#B3B6B7')
plt.tight_layout()
plt.show()
# endregion



# region Kalori Yoğunluğu Analizi
df['cal_density'] = df['calories'] / (df['fat'] + df['carb'] + df['protein'])
density = df.groupby('type')['cal_density'].mean().sort_values()

plt.figure(figsize=(10,6))
bars = plt.bar(density.index, density, color='#D4AC0D', edgecolor='black', alpha=0.8)
plt.axhline(df['cal_density'].mean(), color='#2E7D32', linestyle='--', linewidth=2, label='Genel Ortalama')

plt.title('Kategori Bazlı Kalori Yoğunluğu', fontsize=16, color='#1B4F72', fontweight='bold')
plt.xlabel('Ürün Tipi')
plt.ylabel('Kalori Yoğunluğu')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
# endregion



# region Health Index Analizi
df['health_index'] = (df['protein'] + df['fiber']) / (df['fat'] + df['carb'] + 1)
top10 = df.nlargest(10, 'health_index')

plt.figure(figsize=(10,6))
plt.barh(top10['item'], top10['health_index'], color='#2E7D32', edgecolor='black')
plt.title('En Sağlıklı 10 Ürün (Health Index)', fontsize=16, color='#1B4F72', fontweight='bold')
plt.xlabel('Health Index (Protein + Fiber) / (Fat + Carb + 1)')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.4, color='#B3B6B7')
plt.tight_layout()
plt.show()
# endregion



# region Protein - Karbonhidrat Karşılaştırması
avg_macros = df.groupby('type')[['protein','carb']].mean()

plt.figure(figsize=(10,6))
width = 0.35
x = range(len(avg_macros))
plt.bar(x, avg_macros['protein'], width, label='Protein', color='#2E7D32')
plt.bar([p + width for p in x], avg_macros['carb'], width, label='Karbonhidrat', color='#D4AC0D')

plt.xticks([p + width/2 for p in x], avg_macros.index, rotation=15)
plt.title('Kategori Bazlı Protein ve Karbonhidrat Karşılaştırması', fontsize=16, color='#1B4F72', fontweight='bold')
plt.xlabel('Ürün Tipi')
plt.ylabel('Ortalama Miktar (g)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
# endregion