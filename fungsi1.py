#!/usr/bin/python
def fungsi_tanpa_parameter():
	for i in range(1,5):
		print "looping ke -", i

def fungsi_berparameter(batas_akhir):
	for i in range(1,batas_akhir):
		print "looping ke -", i

print "contoh penggunaan fungsi tanpa parameter"
print "hasil :", fungsi_tanpa_parameter()

print "\n"

print "contoh penggunaaan fungsi berparameter"
print "hasil :",fungsi_berparameter(10)
