#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import pyglet
import glib

class soundPlayer:
    global file
    file = "sound.mp3"
    global player
    player = pyglet.media.Player()

    def play_mus(self):
        music = pyglet.resource.media(file)
        music.play()
        pyglet.app.run()

class makeWindow:
    

    #Foll
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
        
    def destroy(self, widget, data=None):
        gtk.main_quit()
    
    def on_key_press(self, widget, event):
        a = gtk.gdk.keyval_name(event.keyval).isdigit()
        if a:
            print 'digit'
            
    def on_play(self, widget):      
        sound_player = soundPlayer()
        sound_player.play_mus()
           
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
        self.b_quit = gtk.Button("Loka forriti")
            
        #Events
        self.window.connect("key-press-event",self.on_key_press)
        self.b_play.connect("clicked",self.on_play)
        self.b_quit.connect_object("clicked", gtk.Widget.destroy, self.window)
            
        #adding and showing
        self.window.add(self.vbox1)
        self.vbox1.add(self.hbox1)
        self.hbox1.add(self.b_play)
        self.hbox1.add(self.b_pause)
        self.hbox1.add(self.b_quit)
        self.window.show_all()
        

    def main(self):
        gtk.main()

if __name__ == "__main__":
    win = makeWindow()
    win.main()

