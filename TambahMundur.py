def TambahMundur(angka1,angka2):
    if int(angka1) < 359999: #untuk memnfilter agar tidak inputan tidak terlalu besar
        change = 0
        while int(angka1) > 0: #menggunakan while loop utk melakukan pembalikan
            start = int(angka1) % 10 #digunakan untuk menyimpan digit terakhir
            change = (change * 10) + start #digunakan untuk menyimpan digit terakhir diikut digit selanjutnya
            angka1 = int(angka1) // 10 #untuk mengambil sisa digit yg blm diambil
    else:
        print('Invalid Input!') #jika inputan tidak integer
    if int(angka2) < 359999: #untuk memnfilter agar tidak inputan tidak terlalu besar
        change2 = 0
        while int(angka2) > 0: #menggunakan while loop utk melakukan pembalikan
            start2 = int(angka2) % 10 #digunakan untuk menyimpan digit terakhir
            change2 = (change2 * 10) + start2 #digunakan untuk menyimpan digit terakhir diikut digit selanjutnya
            angka2 = int(angka2) // 10 #untuk mengambil sisa digit yg blm diambil
    else:
        print('Invalid Input!') #jika inputan tidak integer

    hasil = change + change2 #melakukan perhitungan hasil pembalikan

    change3 = 0
    while hasil > 0: #menggunakan while loop utk melakukan pembalikan
        start3 = hasil % 10 #digunakan untuk menyimpan digit terakhir
        change3 = (change3 * 10) + start3 #digunakan untuk menyimpan digit terakhir diikut digit selanjutnya
        hasil = hasil // 10 #untuk mengambil sisa digit yg blm diambil
    print(change3) #mencetak hasil perhitungan yg sudah dibalik

x = (input('Masukkan angka 1 : '))
y = (input('Masukkan angka 2 : '))
TambahMundur(x,y)