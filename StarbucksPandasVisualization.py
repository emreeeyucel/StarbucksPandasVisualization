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
ax.tick_params(axis='y', labelsize=12)                         #  axis = hangi eksen olduğu eksendeki etiketlerin yazı tipi boyutunu büyütür veya küçültür.
ax.tick_params(axis='x', labelsize=12)
plt.xticks(rotation=0, fontweight='light', fontsize=12)
plt.yticks(fontweight='light', fontsize=12)

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