#!/usr/bin/python
def cetak_biodata(nama,universitas,umur=20):
	print "Nama :",nama
	print "Umur :",umur
	print "Sekolah :",universitas
	return;

print "*******************************"
print "Tanpa Memakai Default Argument"
print "*******************************"
cetak_biodata(nama="Muhamad Dani Ramanda",umur=19,universitas="IBI Darmajaya")

print "\n"

print "*******************************"
print "Memakai Default Argument"
print "*******************************"
cetak_biodata(nama="Muhamad Dani Ramanda",universitas="IBI Darmajaya")
