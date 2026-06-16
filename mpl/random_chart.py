import random
import matplotlib.pyplot as plt

# 1. Adım: 1 ile 12 arasında 12 adet rastgele tam sayı üretme
random_values = [random.randint(1, 12) for _ in range(12)]
months = list(range(1, 13))

# 2. Adım: Çizgi Grafik Oluşturma
plt.plot(months, random_values, marker='o', linestyle='-', color='b')

# 3. Adım: Grafik Özelliklerini Ayarlama
plt.xlabel('Aylar (Months)')
plt.ylabel('Değerler (Values)')
plt.title('the random values')
plt.xticks(months)
plt.grid(True)

# 4. Adım: Grafiği ekranda POP-UP penceresi olarak gösterme
# Bu komut satırı, kodu çalıştırdığınızda grafiği etkileşimli bir pencerede açar.
plt.show()