#!/usr/bin/python

def fungsi_tanpa_parameter():
	temp = 0
	for i in range(1,5):
		temp = temp + i
	return temp

def fungsi_parameter(batas):
	temp = 0
	for i in range(1,batas):
		temp = temp + i
	return temp

print "contoh penggunaan fungsi tanpa parameter"
print "hasil:",fungsi_tanpa_parameter()
print "hasil:",fungsi_tanpa_parameter()
print "hasil:",fungsi_tanpa_parameter()

print "\n"

print "contoh penggunaan fungsi dengan parameter"
print "hasil:",fungsi_parameter(10)
print "hasil:",fungsi_parameter(12)
print "hasil:",fungsi_parameter(15)



