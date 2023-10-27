import os
from video_fullscreen import fullscreen
from TalkFunction import *
from PIL import Image, ImageTk
import PIL.Image
from itertools import count
import tkinter as tk
from loadingfun import *




def learn():
    # First: Alphabets:
    try:
        loading("audio/17.mp3", "photos_GUI/yo.gif", 6000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/Letters.mp4")

    # Then Numbers:
    # Numbers from 1 to 10:
    
    try:
        loading("audio/18.mp3", "photos_GUI/yo.gif", 6000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/Numbers from 1 to 10.mp4")
    # Numbers from 10 to 100:
    try:
        loading("audio/19.mp3", "photos_GUI/yo.gif", 8000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/Numbers from 10 to 100.mp4")

    # Then Colors:
    try:
        loading("audio/20.mp3", "photos_GUI/yo.gif", 6000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/Colors.mp4")

    # Then Emojis:
    try:
        loading("audio/21.mp3", "photos_GUI/yo.gif", 6000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/Emojis.mp4")

    # Then shapes:
    try:
        loading("audio/22.mp3", "photos_GUI/yo.gif", 6000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/shapes.mp4")

    # Then fruits:
    try:
        loading("audio/23.mp3", "photos_GUI/yo.gif", 6000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/fruits.mp4")

    # Then ablution:
    try:
        loading("audio/25.mp3", "photos_GUI/yo.gif",8000,2,200)
    except:
        pass
    fullscreen("Learn/Videos/ablution.mp4")

    # Then Praying:
    try:
        loading("audio/26.mp3", "photos_GUI/yo.gif", 8000,2,200)
    except:
        pass
    # Last Praying:
    fullscreen("Learn/Videos/praying.mp4")



