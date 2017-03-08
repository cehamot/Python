#!/usr/bin/python

print "***********************"
print "Aplikasi Login"
print "***********************"

username=raw_input("Username = ")
password=raw_input("Password = ")

username_from_db="admin"
password_from_db="dani"

if username == username_from_db:
	if password == password_from_db:
		print "Sukses Login"
	else:
		print "User Tidak Terdaftar"
else:
	print "Password Salah"
	print "EH SALAH PASSWORD"
