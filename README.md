# praktikum-10
## Bahasa Pemrograman (Tugas Pertemuan 10)

### Program Menampilkan Nilai (Tugas, UTS, UAS, Nilai Akhir) dengan DICTIONARY
* FLOWCHART :
* ![img](https://github.com/raissaputra/praktikum-09/blob/main/assets/flowchart.png)
* OUTPUT PROGRAM `inputNilai.py`:
* ![img](https://github.com/raissaputra/praktikum-10/blob/main/praktikum/assets/lihat.png)
* ![img](https://github.com/raissaputra/praktikum-10/blob/main/praktikum/assets/tambah.png)
* ![img](https://github.com/raissaputra/praktikum-10/blob/main/praktikum/assets/finish.png)
  *  Inisialisasi variabel untuk menampung nilai inputan dari user:
  * ```
    nim = []
    nama = []
    uts = []
    uas = []
    tugas = []
    akhir = []
    ```
  * Menggunakan perulangan `While` dan `Dictionary` untuk programnya.
    - selama bernilai true program akan looping terus
    - inputan user berupa huruf depan yang ada di menu.
    - jika L or l, maka akan melihat data yang tersedia.
    - jika T or t, maka akan menambah data sesuai dari user.
    - jika U or u, maka ubah data.
    - jika H or h, untuk hapus data.
    - jika C or c, untuk cari data.
    - jika K or k, keluar
    - untuk tambah data dengan metod append() dan key:values dictionary, berikut programnya:
      ```
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
      ```
    - unutk melihat hasil tambah data maka pilih menu L or l, berikut kode nya:
    - 
      ```
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
      ```
     
* OUTPUT PROGRAM `latihan1.py`:
* ![img](https://github.com/raissaputra/praktikum-10/blob/main/praktikum/assets/latihan.png)
