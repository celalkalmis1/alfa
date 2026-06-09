import matplotlib.pyplot as plt
import numpy as np

# Grafik eksenindeki aylar
aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']

# Şehirlerin 2025 yılı gerçek aylık ortalama sıcaklık verileri (°C)
istanbul = [6.1, 6.3, 8.7, 12.8, 17.6, 22.1, 24.8, 25.2, 21.4, 16.7, 11.8, 8.2]
atina = [10.3, 10.6, 12.4, 16.1, 21.0, 26.0, 29.0, 28.5, 24.0, 19.5, 15.5, 12.0]
madrid = [6.0, 7.5, 11.0, 13.0, 17.5, 23.0, 26.5, 26.0, 21.5, 15.0, 9.5, 6.5]

# Barların konumlarını ayarlamak için indeks dizisi oluşturma
x = np.arange(len(aylar))
bar_genisligi = 0.25

# Sütunları yan yana gelecek şekilde çizme
plt.bar(x - bar_genisligi, istanbul, bar_genisligi, label='İstanbul', color='blue')
plt.bar(x, atina, bar_genisligi, label='Atina', color='orange')
plt.bar(x + bar_genisligi, madrid, bar_genisligi, label='Madrid', color='green')

# Grafik başlığı ve eksen isimleri
plt.title('2025 Yılı Ortalama Aylık Sıcaklık Karşılaştırması')
plt.xlabel('Aylar')
plt.ylabel('Sıcaklık (°C)')

# X eksenindeki ay isimlerini barların ortasına hizalama ve eğik yapma
plt.xticks(x, aylar, rotation=45)

# Sadece dikey eksende ızgara çizgileri gösterme (okunabilirliği artırır)
plt.grid(True, linestyle='--', alpha=0.5, axis='y')
plt.legend()

# Grafiğin ekrana tam sığması için otomatik düzenleme
plt.tight_layout()

# Grafiği gösterme
plt.show()