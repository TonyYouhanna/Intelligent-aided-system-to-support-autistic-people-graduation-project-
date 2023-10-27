from TalkFunction import *
import os
from sub_window import *
from PIL import Image, ImageTk
import PIL.Image
from itertools import count
import tkinter as tk
import time
from loadingfun import *


########################################

def start_project():
    # Import the facial Expression
    from Expression.FacialExpression import read_face
    # Use Facial expression Function
    output = read_face()
    return output

def spin_game():
    # Import the Spin Game
    import Games.SpinGame as sp
    # Spin ball Game
    sp.spinGame()

def cardgame():
    # Import the card Game
    from Games.Card_Game.cardgame import card_game
    # Car Game
    card_game()

def car_game():
    # Import the card Game
    from Games.CarGame.CarGame import cargame
    # Car Game
    cargame()

def snake_game():
    # Import the Snake Game
    from Games.SnakeGame.Snakegame import snake_game
    # Snake Game
    snake_game()

def virtual_paint():
    # Import the virtual paint
    from Games.Virtual_Paint.Paint import paint
    # paint
    paint()

def start_learn():
    # Import learn
    from Learn.Start_Learn import learn
    # Learn
    learn()

def Main():
    feeling = [0, 0, 0, 0, 0]
    while True:

        try:
            loading("audio/2.wav", "photos_GUI/cute.gif", 7000,4,100)

        except:
            pass


        max_index = start_project()
        while max_index == 0:
            feeling[0] = feeling[0] + 1
            # if the kid is happy the start_project function will return 0 and according to it.
            # we will start the next program
            try:
                loading("audio/4.wav", "photos_GUI/cute.gif", 7000,4,100)
            except:
                pass


            try:
                loading("audio/11.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass





            try:
                snake_game()

            except:
                pass

            try:
                loading("audio/10.wav", "photos_GUI/last.gif", 4000,28,30)

            except:
                pass



            try:
                spin_game()
            except:
               pass



            # Learn (Alphabet, Numbers, Colors, ablution, Praying)

            try:
                loading("audio/12.wav", "photos_GUI/yo.gif", 5000,2,200)
            except:
                pass




            try:
                start_learn()
            except:
                pass

            time.sleep(1)

            try:
                loading("audio/14.wav", "photos_GUI/last.gif", 6000,28,30)

            except:
                pass




            # Painting
            try:
                virtual_paint()
            except:
                pass


            try:
                loading("audio/6.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass





            # Card game
            # try:
            #     loading("audio/7.wav", "photos_GUI/last.gif", 5000,28,30)
            #     cardgame()
            # except:
            #     pass



            # Car game

            try:
                loading("audio/8.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            


            try:
                car_game()
            except:
                pass
            break

        while max_index == 1:
            feeling[1] = feeling[1] + 1
            # if the kid is neutral the start_project function will return 1 and according to it.

            try:
                loading("audio/9.wav", "photos_GUI/cute.gif", 5000,4,100)
            except:
                pass
            # try:
            #     loading("audio/10.wav", "photos_GUI/last.gif", 4000,28,30)
            # except:
            #     pass

            # Spin Game
           # try:
           #     spin_game()
           # except:
           #     pass

            time.sleep(1)

            # Car game
            try:

                loading("audio/8.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                car_game()
            except:
                pass

            # Snake game
            try:
                loading("audio/11.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass

            try:
                snake_game()
            except:
                pass

            # Learn (Alphabet, Numbers, Colors, ablution, Praying)
            try:
                loading("audio/12.wav", "photos_GUI/yo.gif", 5000,2,200)
            except:
                pass

            try:
                start_learn()
            except:
                pass

            # Painting
            try:
                loading("audio/14.wav", "photos_GUI/last.gif", 6000,28,30)

            except:
                pass
            try:
                virtual_paint()
            except:
                pass

            # Card game
            try:
                loading("audio/7.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                cardgame()
            except:
                pass
            break

        while max_index == 2:
            feeling[2] = feeling[2] + 1
            # if the kid is angry the start_project function will return 2 and according to it.
            # Car game
            try:
                loading("audio/angry.wav", "photos_GUI/cute.gif", 9000,4,100)
            except:
                pass
            try:
                loading("audio/13.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass

            try:
                car_game()
            except:
                pass

            # Painting
            # try:
            #     loading("audio/14.wav", "photos_GUI/last.gif", 6000,28,30)
            #     virtual_paint()
            # except:
            #     pass

            # Learn (Alphabet, Numbers, Colors, ablution, Praying)
            try:
                loading("audio/12.wav", "photos_GUI/yo.gif", 5000,2,200)
            except:
                pass
            try:
                start_learn()
            except:
                pass

            # Snake game
            try:
                loading("audio/11.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                snake_game()
            except:
                pass

            # Card game
            # try:
            #     loading("audio/7.wav", "photos_GUI/last.gif", 5000,28,30)
            #
            #     cardgame()
            # except:
            #     pass

            # Spin Game
            # try:
            #     loading("audio/10.wav", "photos_GUI/last.gif", 4000,28,30)
            # except:
            #     pass

           # try:
            #    spin_game()
          # except:
          #       pass
            break

        while max_index == 3:
            feeling[3] = feeling[3] + 1
            # if the kid is surprised the start_project function will return 3 and according to it.
            try:
                loading("audio/27.mp3", "photos_GUI/cute.gif", 5000,4,100)
            except:
                pass
            # Painting
            try:
                loading("audio/14.wav", "photos_GUI/last.gif", 6000,28,30)

            except:
                pass
            try:
                virtual_paint()
            except:
                pass

            # Card game
            try:
                loading("audio/6.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                cardgame()
            except:
                pass

            # Spin Game
            # try:
            #     loading("audio/10.wav", "photos_GUI/last.gif", 4000,28,30)
            #
            # except:
            #     pass
            #try:
             #   spin_game()
          #  except:
           #     pass

            # Car game
            try:
                loading("audio/8.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                car_game()
            except:
                pass

            # Learn (Alphabet, Numbers, Colors, ablution, Praying)
            try:
                loading("audio/12.wav", "photos_GUI/yo.gif", 5000,2,200)
            except:
                pass
            try:
                start_learn()
            except:
                pass

            # Snake game
            try:
                loading("audio/11.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                snake_game()
            except:
                pass
            break

        while max_index == 4:
            feeling[4] = feeling[4] + 1
            # if the kid is sad the start_project function will return 3 and according to it.
            # Card game
            try:
                loading("audio/16.wav", "photos_GUI/cute.gif", 5000,4,100)
            except:
                pass
            try:
                loading("audio/6.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                cardgame()
            except:
                pass

            # Snake game
            try:
                loading("audio/11.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                snake_game()
            except:
                pass

            # Learn (Alphabet, Numbers, Colors, ablution, Praying)
            try:
                loading("audio/12.wav", "photos_GUI/yo.gif", 5000,4,200)
            except:
                pass
            try:
                start_learn()
            except:
                pass

            # Spin Game
            try:
                loading("audio/10.wav", "photos_GUI/last.gif", 4000,28,30)

            except:
                pass
            try:
                spin_game()
            except:
                pass

            # Car game
            try:
                loading("audio/6.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                car_game()
            except:
                pass

            # Painting
            try:
                loading("audio/15.wav", "photos_GUI/last.gif", 5000,28,30)
            except:
                pass
            try:
                virtual_paint()
            except:
                pass
            break
        break
#Main()