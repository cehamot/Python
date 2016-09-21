#!/usr/bin/env python

import sys
import pygame
import pygame.camera
from pygame.locals import*

#ukuran display webcam.
SCREEN_SIZE=(480, 480)

#aktifkan module ptgame dan module camera
pygame.init()
pygame.camera.init()

#deteksi keberadaan kamera,
camera_list = pygame.camera.list_cameras()
if not camera_list:
	print 'Tidak Ada Kamera Terdeteksi'
	sys.exit(0)
	
#buat sebuah layar untuk menampung streaming webcam
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Streaming WebCam with Python')

#aktifkan kamera
camera = pygame.camera.Camera(camera_list[0],SCREEN_SIZE)
camera.start()

#buat loop sehingga kamera terus terupdate
while True:

	#apabila kita klik tombol close pada window
	#maka program akan berhenti
	for event in pygame.event.get():
	   if event.type == QUIT:
	      sys.exit(0)

	#ambil gambar dari kamera
	image = camera.get_image()

	#masukan gambar ke layar
	screen.blit(image,(0,0))

	#update layar sehingga terjadi live streaming
	pygame.display.update()

