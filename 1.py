#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import pygtk
pygtk.require('2.0')
import gtk
import pygst
pygst.require('0.10')
import gst

class soundPlayer:

    def __init__(self):
        self.player = gst.element_factory_make("playbin2", "player")
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        self.player.set_property("video-sink", fakesink)

    def start(self):
        filepath = '/home/heimir/github/Hljodskraaspilari/sound.mp3'
        if os.path.isfile(filepath):
            self.player.set_property("uri", "file://" + filepath)
            self.player.set_state(gst.STATE_PLAYING)
        else: 
            print "Skrá fannst ekki."

    def stop(self):
        self.player.set_state(gst.STATE_NULL)

class makeWindow:

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
        
    def destroy(self, widget, data=None):
        gtk.main_quit()
    
    def on_play(self, widget):      
        self.sound_player.start()

    def on_stop(self,widget):
        self.sound_player.stop()
        
    #PyGtk
    def __init__(self):

        self.sound_player = soundPlayer()

        #Widgets
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        
        self.vbox1 = gtk.VBox()
        self.hbox1 = gtk.HBox()
        
        #Buttons
        self.b_play = gtk.Button('play')
        self.b_stop = gtk.Button('stop')
        self.b_quit = gtk.Button("Loka forriti")
            
        #Events
        self.b_play.connect("clicked", self.on_play)
        self.b_stop.connect("clicked", self.on_stop)
        self.b_quit.connect_object("clicked", gtk.Widget.destroy, self.window)
            
        #adding and showing
        self.window.add(self.vbox1)
        self.vbox1.add(self.hbox1)
        self.hbox1.add(self.b_play)
        self.hbox1.add(self.b_stop)
        self.hbox1.add(self.b_quit)
        self.window.show_all()
        

    def main(self):
        gtk.main()

if __name__ == "__main__":
    win = makeWindow()
    win.main()

