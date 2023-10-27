import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import os
from itertools import count
from Learn.LearnIndevidual import *
from Games.PlayIndevidual import *
from MainProject import *
import time
from loadingfun import *
import pygame
import speech_recognition as sr
from TalkFunction import talk
##################################







###################################################

############################################# GIF CLASS
class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):

        if isinstance(im, str):
            im = PIL.Image.open(im)

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

            self.delay = 20

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

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes('-fullscreen', True)
        # self.title_font = tkfont.Font(family=, size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Pagethree, Pagefour, Pagefive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

####################################################



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        main(self,"photos_GUI/last.gif","audio/1.wav",10000)
        time.sleep(10)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print("Talk")
            pygame.mixer.init()
            pygame.mixer.music.load("audio/0.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
            pygame.quit()
            audio_text = r.listen(source)
            # print("Time over, thanks")
            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

            try:
                # using google speech recognition
                name = r.recognize_google(audio_text)
                # print(type(name))
                # print("Text: " + name)
                talk("Welcome " + name, "temporary.mp3", 3)
                os.remove("temporary.mp3")
            except:
                # print("Sorry, I did not get that")
                pygame.mixer.init()
                pygame.mixer.music.load("audio/error.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.quit()
                pass
        lbl = ImageLabel(self)
        lbl.pack(side="top")
        lbl.load("photos_GUI/main.gif")
        label = tk.Label(self, text="Hi, my name is Bebo im here to have fun with you , are you ready ? ",
                         font=("Times New Roman", 20, "italic", "bold"), fg="#2471A3")
        label.pack(side="top", fill="x", pady=10)
        label.place(x=30,y=400)
        button1 = tk.Button(self, text="Ready",
                            command=lambda: controller.show_frame("Pagefive"), font=("Times New Roman", 25, "bold"),
                            bg="#D031A2", fg="white")

        button1.pack(side="top", pady=20)
        button1.place(x=350, y=500)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Hey friend , Choose !", font=("Times New Roman", 25, "italic", "bold"),
                         fg="#2471A3")
        label.pack(side="top", fill="x", pady=10)

        lbl = ImageLabel(self)
        lbl.pack(anchor=W)
        lbl.place(x=-10, y=65)
        lbl.load("photos_GUI/learnnew.gif")

        button1 = tk.Button(self, text="Let's Learn",
                            command=lambda: controller.show_frame("PageTwo"), font=("Times New Roman", 20, "bold"),
                            bg="#286E7C", fg="white")

        button1.pack(anchor=SW, pady=20)
        button1.place(x=80, y=430)

        button2 = tk.Button(self, text=" Let's Play", command=lambda: controller.show_frame("Pagethree"),
                            font=("Times New Roman", 20, "bold"), bg="#F1C40F", fg="white")
        button2.pack(anchor=E, pady=20)
        button2.place(x=550, y=430)

        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("Pagefive"), font=("Times New Roman", 25, "bold"),
                            bg="#99A3A4", fg="white")

        button3.pack(pady=20)
        button3.place(x=350, y=500)

        lbl = ImageLabel(self)
        lbl.pack(anchor=E)
        lbl.place(x=435, y=65)
        # lbl1.place(x=0,y=100)

        lbl.load("photos_GUI/playnew.gif")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        # button1
        ############################################################
        button1 = tk.Button(self, text="Alphabets",
            command=lambda:Alphabet(), font=("Times New Roman", 20, "bold"),
                            bg="#1A0ECF", fg="white")
        button1.pack(anchor=SW, pady=20)
        button1.place(x=120, y=40)
        # Create a window and pass it to videoGUI Class



        ##########################################################
        # button2

        button2 = tk.Button(self, text="Numbers From 1 to 10",
                            command=lambda: numbersdigits(), font=("Times New Roman", 20, "bold"),
                            bg="#F4D03F", fg="white")
        button2.pack(anchor=SW, pady=20)
        button2.place(x=54, y=140)

        #############################################################
          # button3


        button3 = tk.Button(self, text="Numbers From 10 to 100",
                            command=lambda: numberstens(), font=("Times New Roman", 20, "bold"),
                            bg="#CF220E", fg="white")
        button3.pack(anchor=SW, pady=20)
        button3.place(x=50, y=250)

        ###########################################################
         # button4


        button4 = tk.Button(self, text="Colors",
                            command=lambda: colors(), font=("Times New Roman", 20, "bold"),
                            bg="#8E44AD", fg="white")
        button4.pack(anchor=SW, pady=20)
        button4.place(x=135, y=360)

        ##########################################################
        def Emojis():  # button5
            print("Emojis")

        button5 = tk.Button(self, text="Emojis",
                            command=lambda: Emojies(), font=("Times New Roman", 20, "bold"),
                            bg="#2ECC71", fg="white")
        button5.pack(anchor=SW, pady=20)
        button5.place(x=135, y=460)

        ########################################################
         # button6


        button6 = tk.Button(self, text="Ablution",
                            command=lambda: ablution(), font=("Times New Roman", 20, "bold"),
                            bg="#1A0ECF", fg="white")
        button6.pack(anchor=E, pady=20)
        button6.place(x=605, y=40)

        #############################################################
          # button7


        button7 = tk.Button(self, text="praying",
                            command=lambda: LastPraying(), font=("Times New Roman", 20, "bold"),
                            bg="#F4D03F", fg="white")
        button7.pack(anchor=E, pady=20)
        button7.place(x=606, y=140)

        #############################################################

          # button8


        button8 = tk.Button(self, text="Shapes",
                            command=lambda: Shapes(), font=("Times New Roman", 20, "bold"),
                            bg="#CF220E", fg="white")
        button8.pack(anchor=E, pady=20)
        button8.place(x=610, y=250)

        ################################################################
          # button9


        button9 = tk.Button(self, text="Fruits",
                            command=lambda: Fruits(), font=("Times New Roman", 20, "bold"),
                            bg="#8E44AD", fg="white")
        button9.pack(anchor=E, pady=20)
        button9.place(x=609, y=360)

        ####################################################################


        ##############################################################

        # back button

        buttonback = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame("PageOne"), font=("Times New Roman", 25, "bold"),
                               bg="#99A3A4", fg="white")
        buttonback.pack(anchor=SW, pady=20)
        buttonback.place(x=350, y=500)
        ######################################################


class Pagethree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

         # button1


        button1 = tk.Button(self, text="Spinball Game",
                            command=lambda: Start_SpinGame(), font=("Times New Roman", 30, "bold"),
                            bg="#1A0ECF", fg="white")
        button1.pack(anchor=SW, pady=20)
        button1.place(x=50, y=50)

        ##########################################################
           # button2


        button2 = tk.Button(self, text="Paint Game",
                            command=lambda: Start_Paint(), font=("Times New Roman", 30, "bold"),
                            bg="#F4D03F", fg="white")
        button2.pack(anchor=SW, pady=20)
        button2.place(x=80, y=230)

        #############################################################

        #############################################################
          # button3


        button3 = tk.Button(self, text="Car Game",
                            command=lambda: Start_CarGame(), font=("Times New Roman", 30, "bold"),
                            bg="#CF220E", fg="white")
        button3.pack(anchor=SW, pady=20)
        button3.place(x=500, y=50)

        ###########################################################

        # button4



        button4 = tk.Button(self, text="Card Game",
                            command=lambda: Start_CardGame(), font=("Times New Roman", 30, "bold"),
                            bg="#8E44AD", fg="white")
        button4.pack(anchor=SW, pady=20)
        button4.place(x=495, y=230)
        ######################################################
        # button5

        button5 = tk.Button(self, text="Snake Game",
                            command=lambda: Start_SnakeGame(), font=("Times New Roman", 30, "bold"),
                            bg="#2ECC71", fg="white")
        button5.pack(anchor=SW, pady=20)
        button5.place(x=270, y=380)

        #########################################################






        buttonback = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame("PageOne"), font=("Times New Roman", 25, "bold"),
                               bg="#99A3A4", fg="white")
        buttonback.pack(anchor=SW, pady=20)
        buttonback.place(x=350, y=500)

    ####################################################################


class Pagefour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        button1 = tk.Button(self, text="select",
                            command=lambda: Alphabet())


        button1.pack()

        # button2 = tk.Button(self, text="stop",
        #                    command=quit() )

        #button2.pack()
        button3 = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))

        button3.pack()


class Pagefive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        lbl = ImageLabel(self)
        lbl.pack(anchor=W)
        lbl.place(x=-10, y=40)
        lbl.load("photos_GUI/happynew.gif")
        ############################################################33
          # button1



        button1 = tk.Button(self, text="Let's go together",
                                command=lambda: Main(), font=("Times New Roman", 20, "bold"), bg="#286E7C", fg="white")

        button1.pack(anchor=SW, pady=20)
        button1.place(x=50, y=430)

        button2 = tk.Button(self, text=" Choose by yourself", command=lambda: controller.show_frame("PageOne"),
                            font=("Times New Roman", 20, "bold"), bg="#F1C40F", fg="white")
        button2.pack(anchor=E, pady=20)
        button2.place(x=490, y=430)

        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("StartPage"), font=("Times New Roman", 25, "bold"),
                            bg="#99A3A4", fg="white")

        button3.pack(pady=20)
        button3.place(x=350, y=500)

        lbl = ImageLabel(self)
        lbl.pack(anchor=E)
        lbl.place(x=435, y=40)
        # lbl1.place(x=0,y=100)

        lbl.load("photos_GUI/choosenew.gif")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

