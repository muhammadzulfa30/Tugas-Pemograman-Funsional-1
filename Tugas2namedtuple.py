from collections import namedtuple
Barang = namedtuple('Barang', ('nama_barang', 'harga_jual', 'tersedia_barang'))
Barang1 = Barang('keyboard', 500, True)
Barang2 = Barang('mouse', 700, True)
Barang3 = Barang('headset', 800, True)
Barang4 = Barang('Laptop', 1200, False)
print(f'barang4: {Barang4}')