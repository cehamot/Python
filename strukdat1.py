#!/usr/bin/python
#cara mendefinisikan list
sebuah_list=['Ubuntu',
		'freebsd',
		'Debian',
		'Backbox',
		'fedora']

#cara mendefiniksan tuple
sebuah_tuple = (0,1,2,3,4,5,6)

#cara mendefinisikan dictoniary
sebuah_dict = {'nama':'Muhamad Dani Ramanda',
		'prodi': 'Informatics Engineering',
		'email':'muhamaddani3004@gmail.com'}
###############################################

#cara menambahkan data baru
print "***menambahkan data baru*****"
print sebuah_list
list_baru= sebuah_list + ['PC Linux','Raspberyy Pi','BlankOn']
print list_baru
print "\n"


print sebuah_tuple
tuple_baru = sebuah_tuple + (100,200,300)
print tuple_baru
print "\n"

print sebuah_dict
dict_baru = {'kontak':'085768355930','Alamat':'Jalan Abdul Kadir'}
sebuah_dict.update(dict_baru)
print sebuah_dict 
print "\n"
################################################

#membandingkan yang lama dengan yang baru
print "membandingkan yang lama dengan yang baru"
print "sebuah_list banding list_baru :",cmp(sebuah_list, list_baru)
print "sebuah_tuple banding tuple_baru :",cmp(sebuah_tuple, tuple_baru)
print "sebuah_dict banding dict_baru :",cmp(sebuah_dict,dict_baru)
print "\n"

#mencari nilai max dan min
print "mencari nilai max dan min"
print "coba perikas sebuah_list:"
print "max:",max(sebuah_list)
print "min:",min(sebuah_list)
