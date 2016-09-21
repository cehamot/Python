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

print "mengakses beberapa elemenn"
print "------------------------------"
print sebuah_list[2:4]
print sebuah_tuple[1:4]

print "\n"

print "mengakses semua elemen dengan looping for :"
print "-------------------------------"
 
for sebuah in sebuah_list:
	print sebuah,
print "\n"

for sebuah in sebuah_tuple:
	print sebuah,
print "\n"


for sebuah in sebuah_dict:
	print sebuah,':',sebuah_dict[sebuah]

print "\n"
################################################

#cara update sebuah elemen :
print "cara update sebuah elemen:"
print "\n"

print sebuah_list
sebuah_list[3]='slackware'
print sebuah_list
print "\n"
