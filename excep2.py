#!/usr/bin/python
sebuah_list= [1,2,3,4,5]
sebuah_tuple= (1,2,3,4,5)
sebuah_direc={'nama':'M Dani Ramanda','email':'muhamaddani3004@gmail.com'}

try:
	print sebuah_list[10]
except IndexError, e:
	print "proses gagal karena :",e
print "proses cetak ini masih dapat di jalankan"

try:
	print sebuah_tuple[10]
except IndexError, e:
	print "proses gagal karena :", e
print "proses cetak ini masih dapat di jalankan"

try:
	print sebuah_direc['website']
except KeyError,e:
	print "proses gagal karena :", e
print "proses cetak ini masih dapat di jalankan"
