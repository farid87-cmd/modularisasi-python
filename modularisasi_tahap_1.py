"""
Program menghitung luas segitiga
luas_segitiga = alas*tinggi / 2
"""
print ('menghitung luas segitiga #1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas= {alas} dan tinggi= {tinggi} memiliki luas {luas_segitiga}')

print ('\nmenghitung luas segitiga dengan copy paste #2')
alas = 20
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas= {alas} dan tinggi= {tinggi} memiliki luas {luas_segitiga}')

print('\nmembuat fungsi luas segitiga')
def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print (f'mengitung segitiga denga fungsi, hasilnya {hitung_luas_segitiga(10,6)}')
print (f'mengitung segitiga denga fungsi, hasilnya {hitung_luas_segitiga(20,6)}')
print (f'mengitung segitiga denga fungsi, hasilnya {hitung_luas_segitiga(30,6)}')

print('\nmembuat fungsi luas segitiga')
def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 6
print (f'mengitung segitiga denga fungsi, alas= {alas} dan tinggi= {tinggi} hasilnya, {hitung_luas_segitiga(10,6)}')
alas = 20
tinggi = 2
print (f'mengitung segitiga denga fungsi, alas= {alas} dan tinggi= {tinggi} hasilnya, {hitung_luas_segitiga(20,2)}')
alas = 30
tinggi = 4
print (f'mengitung segitiga denga fungsi, alas= {alas} dan tinggi= {tinggi} hasilnya, {hitung_luas_segitiga(30,4)}')
