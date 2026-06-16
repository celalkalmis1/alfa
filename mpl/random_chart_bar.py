import random
import matplotlib.pyplot as plt

# 1. Adım: Verileri aynı şekilde hazırlıyoruz
random_values = [random.randint(1, 10) for _ in range(12)]
months = list(range(1, 13))

# 2. Adım: Çizgi yerine Yatay Sütun Grafiği (barh) kullanıyoruz
# plt.barh(y_ekseni, x_ekseni) mantığıyla çalışır.
# İlk yazılan (months) Y eksenine yerleşir, ikinci yazılan (random_values) genişlik olur.
plt.barh(months, random_values, color='skyblue', edgecolor='black')

# 3. Adım: Eksen Etiketlerini Güncelleme
# Grafiği yan çevirdiğimiz için eksen isimlerini de takas ediyoruz.
plt.xlabel('Değerler (Values)')          # Artık X ekseninde sayılar var
plt.ylabel('Aylar (Months)')            # Artık Y ekseninde aylar var
plt.title('the random values')

# 4. Adım: Eksen Çentiklerini Ayarlama
# Aylar artık Y ekseninde olduğu için plt.xticks yerine plt.yticks kullanıyoruz.
plt.yticks(months)

# Izgara çizgilerini sadece dikey (X ekseni boyunca) olacak şekilde ayarlıyoruz
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# 5. Adım: Pop-up olarak ekranda gösterme
plt.show()