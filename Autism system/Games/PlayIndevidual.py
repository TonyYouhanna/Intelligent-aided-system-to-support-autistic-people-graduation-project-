from Games.CarGame import CarGame
from Games.SpinGame import *
from Games.Virtual_Paint.Paint import paint
from Games.Card_Game import cardgame
from Games.SnakeGame.Snakegame import *
from loadingfun import *

def Start_SpinGame():
    try:
        loading("audio/10.wav", "photos_GUI/last.gif", 4000, 28,60)

    except:
        pass
    try:

        spinGame()
    except:
        pass

def Start_CardGame():
    try:
        loading("audio/7.wav", "photos_GUI/last.gif", 5000, 28, 60)
    except:
        pass

    try:
        cardgame.card_game()
    except:
        pass

def Start_CarGame():
    try:
        loading("audio/8.wav", "photos_GUI/last.gif", 5000, 28, 60)
    except:
        pass



    try:
        CarGame.cargame()
    except:
        pass

def Start_SnakeGame():
    try:
        loading("audio/11.wav", "photos_GUI/last.gif", 5000, 28, 60)
    except:
        pass


    try:
        snake_game()
    except:
        pass

def Start_Paint():
    try:
        loading("audio/14.wav", "photos_GUI/last.gif", 6000, 28, 60)

    except:
        pass

    try:
        paint()
    except:
        pass