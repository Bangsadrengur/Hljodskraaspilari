#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import pygtk
pygtk.require('2.0')
import gtk
import pygst
pygst.require('0.10')
import gst

# Notkun: sound_player = soundPlayer()
# Eftir:  sound_player er hlutur sem meðhöndlar afspilun hljóðskráa.
class soundPlayer:

    def __init__(self):
        self.player = gst.element_factory_make("playbin2", "player")
        # Eftirfarandi tvær línur slökkva á hreyfimyndavirkni spilarans.
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        self.player.set_property("video-sink", fakesink)
    
    # Notkun: x.start()
    # Eftir:  Tilgreind skrá hefur verið gangsett eða villutexti er á aðalúttaki.
    def start(self):
        filepath = '/home/heimir/github/Hljodskraaspilari/sound.mp3'
        if os.path.isfile(filepath):
            self.player.set_property("uri", "file://" + filepath)
            self.player.set_state(gst.STATE_PLAYING)
        else: 
            print "Skrá fannst ekki."

    # Notkun: x.stop()
    # Eftir:  Engin spilun hljóðskráar er í gangi.
    def stop(self):
        self.player.set_state(gst.STATE_NULL)

# Notkun: win = makeWindow()
# Meðan:  Klasinn keyrir gluggaumhverfi fyrir hljóðskráaafspilara. Klasinn sér aðeins
#           um gluggana og keyrslu umhverfis.
class makeWindow:

    # Meðhöndlar loknarköll frá gluggaumhverfi.
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
        
    # Meðhöndlar köll í lokun forrits.
    def destroy(self, widget, data=None):
        gtk.main_quit()
    
    # Kallar í fall afspilunarhlutar sem hefur afspilun.
    def on_play(self, widget):      
        self.sound_player.start()

    # Kallar í fall afspilunarhlutar sem stöðvar afspilun.
    def on_stop(self,widget):
        self.sound_player.stop()
        
    # Smiður
    def __init__(self):

        # Afspilunarhlutur smíðaður.
        self.sound_player = soundPlayer()

        #Widgets
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        
        #Boxes
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
        

    # Keyrslufall forrits.
    def main(self):
        #Enginn munur í keyrslu með eða án threads_init. Geymi það þar til hægt er að prufa mun með meiri virkni í forritinu sjálfu.
        gtk.gdk.threads_init()
        gtk.main()

if __name__ == "__main__":
    win = makeWindow()
    win.main()

