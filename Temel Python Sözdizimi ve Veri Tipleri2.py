# Kullanıcının aldığı ürünlerin toplam tutarını hesaplayan basit bir program

urun1 = "Elma"
urun2 = "Armut"
fiyat1 = 3.5    # float
fiyat2 = 4      # int
adet1 = 4       # int
adet2 = 2       # int

# Toplam fiyat hesaplama (sayılarla işlemler)
toplam = (fiyat1 * adet1) + (fiyat2 * adet2)

# Yorum satırı: aşağıdaki çıktı string ve sayı birleştirmesiyle yapılmıştır.
print("Sepetteki ürünler:")
print("- " + urun1 + " x" + str(adet1))  # type casting: int → str
print("- " + urun2 + " x" + str(adet2))

# String metodu: title() → baş harfleri büyük yapar
print("Toplam tutar:", round(toplam, 2))  # float değeri 2 basamakta yuvarlama
print("Ürünler:", urun1.title(), "ve", urun2.title())

# Veri tiplerini yazdır
print("fiyat1 veri tipi:", type(fiyat1))
print("adet1 veri tipi:", type(adet1))
print("toplam veri tipi:", type(toplam))
