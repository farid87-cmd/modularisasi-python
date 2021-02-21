#import geometri.segitiga as sg

from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga
from geometri.persegipanjang import hitung_luas_persegipanjang, info as info_persegipanjang

print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_luas_segitiga(10,3)}')

print(f'\n{info_persegipanjang()}')
print(f'hitung_luas_persegipanjang {hitung_luas_persegipanjang(10,3)}')

 