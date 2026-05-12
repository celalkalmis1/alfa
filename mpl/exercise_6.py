number = int(input("Lütfen faktöriyelini almak istediğiniz sayıyı girin: "))
faktoriel = 1

# range kısmına +1 ekledik ki sayının kendisini de kapsasın
for i in range(1, number + 1):
    # faktoriel değişkenini döngüdeki i sayısı ile çarpıyoruz
    faktoriel *= i

print(f"Sonuç: {faktoriel}")