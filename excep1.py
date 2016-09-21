#!/usr/bin/python
sebuah_angka = 22

try:
	print sebuah_angka / 0
except:
	print "proses perhitungan gagal"

print "proses cetak ini masih dapat di jalankan"

try:
	print sebuah_angka / 0
except ZeroDivisionError, e:
	print "proses perhitungan gagal karena:",e

print "proses cetak ini masih dapat di jalankan"

print sebuah_angka / 0

#jika tidak memakai exception maka proses berikutnya tidak akan dijalankan
print "apakah proses cetak ini masih dapat di jalankan??"
