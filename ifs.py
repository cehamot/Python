#!/usr/bin/python
print "*******************************"
print "Program Suara"
print "*******************************"
vol = int(raw_input('Masukan Volume Suara:'))
if vol < 20:
	print ("Suara terlalu kecil")
elif 20 <= vol < 40:
	print ("Suara Kecil")
elif 40 <= vol < 60:
	print ("suara normal")
elif 60 <= vol < 80:
	print ("suara besar")
elif 80 <= vol < 100:
	print ("suara terlalu besar")
else:
	print ("tidak ada")
