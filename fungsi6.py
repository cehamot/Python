#!/usr/bin/python
def cetak_biodata(nama,twitter,**data_tambahan):
	print "Nama Lengkap :", nama;
	print "Twitter :", twitter;
	print "*****************"
	print "Data Lain nya"
	i = 1
	for data in data_tambahan:
		print "%s : %s" % (data,data_tambahan[data])
	return;

print "hasil cetak biodata :"
cetak_biodata("Muhamad Dani Ramanda","@MdhaniR",email="muhamaddani3004@gmail.com",facebook="Muhamad Dani Ramanda",Telegram="085768355930")	
