from PIL import Image, ImageTk
import PIL.Image
from itertools import count
import tkinter as tk
import pygame


def loading(sound, photo, num, frames, delay):
    def close():
        master.destroy()
        quit()

    def update(ind):
        frame =frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        master.after(delay, update, ind)
    root = tk.Tk()
    root.withdraw()
    master = tk.Toplevel()
    frameCnt = frames
    frames = [tk.PhotoImage(file=photo, format='gif -index %i' % (i)) for i in range(frameCnt)]
    label = tk.Label(master)
    label.pack()
    label.place(x="-5", y="-8")
    master.after(0, update, 0)

    # Show image using label
    master.attributes("-fullscreen", True)
    master['bg'] = "white"
    pygame.mixer.init()  # initialise the pygame
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)
    # winsound.PlaySound(sound, winsound.SND_ASYNC)
    master.after(num, lambda:close() and master.destroy())
    root.mainloop()


####################################################################
