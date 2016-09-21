#!/usr/bin/python
def cetak_nilai(nama,twitter,*scores):
	print "Nama :",nama;
	print "Twitter :",twitter;
	print "Score yang di peroleh :"
	i = 1
	for score in scores:
		print "nilai ke - %d : %d" % (i,score)
		i = i+1

	return;

#kalau parameter di isi semua
print "dengan adanya variable-length variabel sisa akn menjadi tuple :"
cetak_nilai("Dani","@MdhaniR",90,80,80,80,88)

