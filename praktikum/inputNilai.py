nim = []
nama = []
uts = []
uas = []
tugas = []
akhir = []

while True:
    print('Program Input Nilai')
    print('='*25)

    print('[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ')
    pilih = input('Pilih Menu : ')
    if pilih == 'L' or pilih == 'l':
        print('Daftar Nilai')
        print('='*70)
        print('| No |\tNIM\t    |  NAMA   | TUGAS   |  UTS    |  UAS    | AKHIR  |')
        print('='*70)
        print('|                      TIDAK ADA DATA                                |')
        print('='*70, '\n')

        for i in range(len(nim)):
            nm = '| %d. |\t%s\t' % (i+1, nim[i]['nim'])
            im = '    | %s' % nama[i]['nama']
            tg = '     | %.2f' % tugas[i]['tugas']
            ut = '   | %.2f' % uts[i]['uts']
            ua = '   | %.2f' % uas[i]['uas']
            ah = '   | %.2f' % akhir[i]['akhir']
            ln = '  |'

            join = nm + im + tg + ut + ua + ah + ln
            print(join)
        print('='*70, '\n')

    elif pilih == 'T' or pilih == 't':
        print('Tambah Data')
        x_nim = int(input('NIM\t: '))
        nim.append({'nim': x_nim})
        x_nama = str(input('Nama\t: '))
        nama.append({'nama': x_nama})
        x_uts = float(input('Nilai UTS\t: '))
        y_uts = x_uts*(35/100)
        uts.append({'uts': y_uts})
        x_uas = float(input('Nilai UAS\t: '))
        y_uas = x_uas*(35/100)
        uas.append({'uas': y_uas})
        x_tugas = float(input('Nilai Tugas\t: '))
        y_tugas = x_tugas*(30/100)
        tugas.append({'tugas': y_tugas})
        x_akhir = y_uts+y_uas+y_tugas
        akhir.append({'akhir': x_akhir})

    elif pilih == 'U' or pilih == 'u':
        print('Data belum dapat di ubah')
    elif pilih == 'H' or pilih == 'h':
        print('Data belum dapat di hapus')
    elif pilih == 'C' or pilih == 'c':
        print('Pencarian belum tersedia !')
    elif pilih == 'K' or pilih == 'k':
        print('Terimakasih, sudah mencoba')
