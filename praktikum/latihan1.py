dftrKontak = {'Ari': 6281267888, 'Dina': 6287677776}
print('Nama\t| Nomor Telpon')
print('='*22)
for key, value in dftrKontak.items():
    print(key, '\t|', value)

print('\nKontaknya Ari : ', dftrKontak['Ari'])
dftrKontak['Riko'] = 6287654544
dftrKontak['Dina'] = 6288999776
print(dftrKontak.keys())
print(dftrKontak.values())
print(dftrKontak.items())
del dftrKontak['Dina']
print('\n', dftrKontak.items())
