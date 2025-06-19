# Kullanıcıdan ad, doğum yılı ve öğrenci olup olmadığını alır ve bilgilerini işler.

# Yorum satırları kodu okunabilir kılar ve açıklama sağlar.

isim = "Mithat"         # str veri tipi
dogum_yili = 2000       # int veri tipi
boy = 1.75              # float veri tipi
ogrenci_mi = True       # bool veri tipi
telefon = None          # NoneType veri tipi

# String işlemleri
print("Merhaba, " + isim + "!")  # Birleştirme (concatenation)

# Yaş hesaplama
yil = 2025
yas = yil - dogum_yili  # Sayılarla işlem ve matematiksel operatör

print("Yaşınız:", yas)
print("Boyunuz:", boy)

# Veri tipi dönüşümü (type casting)
yas_str = str(yas)
print("Yaşınızı yazıyla ifade edersek: " + yas_str)

# String metotları
print("Adınız büyük harflerle:", isim.upper())
print("Adınız küçük harflerle:", isim.lower())

# Mantıksal kontrol
if ogrenci_mi:
    print("Statünüz: Öğrenci")
else:
    print("Statünüz: Çalışan")

# Değişkenin tipi nedir?
print("Telefon değişkeninin veri tipi:", type(telefon))
