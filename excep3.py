try:
    angka1 = int(raw_input('masukan angka ke-1 :'))
    angka2 = int(raw_input('masukan angka ke-2 :'))

    print 'hasil perhitungan :',angka1/angka2

except ZeroDivisionError,e:
    print "proses pembagian gagal karena :",e
except ValueError,e:
    print "proses perhitungan gagal karena :",e
    print "proses cetak masih dapat di jalankan"
