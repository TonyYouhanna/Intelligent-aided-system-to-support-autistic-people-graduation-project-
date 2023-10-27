
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
from itertools import count
from MainProject import *

#########################################

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):

        if isinstance(im, str):
            im= PIL.Image.open(im)





        self.loc = 0
        self.frames = []


        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


########################################

def main(page,pic,sound,destroy):
        sub = tk.Toplevel(page)
        sub.transient(page) #Keeps sub window on top of root
        sub.minsize(320, 240)

        sub.configure(bg='white')


        sub.attributes("-fullscreen" , True)
        lbl = ImageLabel(sub)
        lbl.pack(anchor=W)
        lbl.load(pic)
        lbl.place(x=-5,y=5)
        sub.after(destroy, lambda: sub.destroy())
        pygame.mixer.init()  # initialise the pygame
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(loops=0)

        pos = []

        def main_move(event):
            #When the main window moves, adjust the sub window to move with it
            if pos:
                sub.geometry("+{0}+{1}".format(pos[0], pos[1]))
                # Change pos[0] and pos[1] to defined values (eg 50) for fixed position from main

        def sub_move(event):
            # Set the min values
            min_w = page.winfo_rootx()
            min_h = page.winfo_rooty()
            # Set the max values minus the buffer for window border
            max_w = page.winfo_rootx() + page.winfo_width() - 15
            max_h = page.winfo_rooty() + page.winfo_height() - 35

            # Conditional statements to keep sub window inside main
            if event.x < min_w:
                sub.geometry("+{0}+{1}".format(min_w, event.y))

            elif event.y < min_h:
                sub.geometry("+{0}+{1}".format(event.x, min_h))

            elif event.x + event.width > max_w:
                sub.geometry("+{0}+{1}".format(max_w - event.width, event.y))

            elif event.y + event.height > max_h:
                sub.geometry("+{0}+{1}".format(event.x, max_h - event.height))

            global pos
            # Set the current sub window position
            pos = [event.x, event.y]

        page.bind('<Configure>', main_move)
        sub.bind('<Configure>', sub_move)




