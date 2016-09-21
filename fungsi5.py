#!/usr/bin/python
def cetak_biodata(nama,kampus,kota):
	print "Nama Lengkap :",nama;
	print "Asal Kampus :",kampus;
	print "Asal Kota : ",kota;

	return;

#kalau tidak memaki keyword argumen : tidak sesuai urutan
print "memakai keyword argumen :"
cetak_biodata("Lampung","darmajaya","dani")

print "\n"

#kalau tidak memakai keyword argumen : sesuai urutan
print "memakai keyword argumen :"
cetak_biodata("M Dani Ramanda","IBI Darmajaya","Bandar Lampung")
