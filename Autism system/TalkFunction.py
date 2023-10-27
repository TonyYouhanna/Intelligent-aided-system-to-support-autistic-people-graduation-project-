import os
import pygame
import time
from gtts import gTTS


def talk(text,loc, num):
    pygame.quit()

    myText = text
    language = "en"
    output = gTTS(text=myText, lang=language, slow=False)
    output.save(loc)
    pygame.mixer.init()
    pygame.mixer.music.load(loc)
    pygame.mixer.music.play()
    time.sleep(num)
    pygame.quit()


