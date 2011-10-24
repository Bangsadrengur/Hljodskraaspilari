#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import pyglet
import glib


class Scanfun:

	#Global Breytur
	global file
	file = "sound.mp3"
	global player
	player = pyglet.media.Player()
	
	
	#Foll
	def delete_event(self, widget, event, data=None):
		return False
		
	def destroy(self, widget, data=None):
		gtk.main_quit()
	
	#def picchange(self, pic):
	#	self.image.set_from_file(pic)

	##notkun: glib.timeout_add_seconds(3, self.on_tick)
	#def on_tick(self):
	
	def on_key_press(self, widget, event):
		a = gtk.gdk.keyval_name(event.keyval).isdigit()
		if a:
			print 'digit'
			
	def on_play(self, widget):		
		music = pyglet.resource.media(file)
		music.play()
		pyglet.app.run()
		   
	#PyGtk
	def __init__(self):
		#Widgets
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)
		self.window.set_border_width(10)
		
		self.vbox1 = gtk.VBox()
		self.hbox1 = gtk.HBox()
		
		self.b_play = gtk.Button()
		self.b_play.set_label('play')
		self.b_pause = gtk.Button()
		self.b_pause.set_label('pause')
			
		#Events
		self.window.connect("key-press-event",self.on_key_press)
		self.b_play.connect("clicked",self.on_play)
			
		#adding and showing
		self.window.add(self.vbox1)
		self.vbox1.add(self.hbox1)
		self.hbox1.add(self.b_play)
		self.hbox1.add(self.b_pause)
		self.window.show_all()
		

	def main(self):
		gtk.main()

if __name__ == "__main__":
	fun = Scanfun()
	fun.main()