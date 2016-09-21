#!/usr/bin/python

angka1=raw_input("Masukan angka pertama = ")
angka1=int(angka1)

angka2=raw_input("masukan angkat kedua =")
angka2=int(angka2)

if angka1==angka2 :
	print "%d sama dengan %d" % (angka1,angka2)
elif angka1!=angka2 :
	print "%d tidak sama dengan %d" % (angka1,angka2)
elif angka1<angka2 :
	print "%d lebih kecil dari %d" % (angka1,angka2)
elif angka1>angka2 :
	print "%d lebih besar dari %d" % (angka1,angka2)
