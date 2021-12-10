dftrKontak = {'Ari': '081267888', 'Dina': '087677776'}
print('Nama\t| Nomor Telpon')
print('='*22)
for key, value in dftrKontak.items():
    print(key, '\t|', value)

# tampilkan kontak ari
print('\nKontaknya Ari : ', dftrKontak['Ari'])
print()
# Tambah kontak baru dengan nama Riko, nomor 087654544
dftrKontak['Riko'] = 6287654544
# Ubah kontak Dina dengan nomor baru 088999776
dftrKontak['Dina'] = 6288999776
# Tampilkan semua Nama
print('Tampilkan semua Nama')
print(dftrKontak.keys())
print()
# Tampilkan semua Nomor
print('Tampilkan semua Nomor')
print(dftrKontak.values())
print()
# Tampilkan daftar Nama dan nomornya
print('Tampilkan daftar Nama dan nomornya')
print(dftrKontak.items())
print()
# hapus kontak dina
del dftrKontak['Dina']
# tampilkan kontak setelah dina dihapus
print('tampilkan kontak setelah dina dihapus')
print(dftrKontak.items())
