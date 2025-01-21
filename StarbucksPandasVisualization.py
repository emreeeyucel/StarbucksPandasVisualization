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



