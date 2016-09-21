#!/usr/bin/python
def sebuah_fungsi():
	angka = 10
	print "di dalam sebuah_fungsi, angka bernilai :",angka

def sebuah_fungsi_lainnya():
	global angka
	angka = 114
	print "dii dalam sebuah_fungsi, angka bernilai :",angka

angka=6666

print "sebuah dipanggil sebuah_fungsi:",angka
sebuah_fungsi()
print "sesudah dipanggil sebuah_fungsi",angka

print "\n"

print "sebelum di panggil sebuah_fungsi_lainnya:",angka
sebuah_fungsi_lainnya()
print "sesudah dipanggil sebuah_fungsi_lainnya:",angka
