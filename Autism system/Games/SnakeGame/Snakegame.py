import math
import os
import time
from TalkFunction import talk
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import random
from loadingfun import *


def snake_game():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    detector = HandDetector(detectionCon=0.8, maxHands=1)

    class SnakeGameClass:
        def __init__(self, foodPath):
            self.points = []  # all points of the snake
            self.lengths = []  # distance between each point
            self.currentLength = 0  # total length of the snake
            self.allowedLength = 150  # total allowed length
            self.previousHead = 0, 0  # previous head point

            self.imgFood = cv2.imread(foodPath, cv2.IMREAD_UNCHANGED)
            self.hFood, self.wFood, _ = self.imgFood.shape
            self.foodPoint = 0, 0
            self.randomFoodLocation()
            self.score = 0

            self.gameOver = False

        def randomFoodLocation(self):
            self.foodPoint = random.randint(100, 600), random.randint(100, 350)

        def update(self, imgMain, currentHead):

            if self.gameOver:
                cvzone.putTextRect(imgMain, "Game Over", [300, 400],
                                   scale=7, thickness=5, offset=20)
                cvzone.putTextRect(imgMain, f'Your Score: {self.score}', [300, 550],
                                   scale=7, thickness=5, offset=20)





            else:
                px, py = self.previousHead
                cx, cy = currentHead

                self.points.append([cx, cy])
                distance = math.hypot(cx - px, cy - py)
                self.lengths.append(distance)
                self.currentLength += distance
                self.previousHead = cx, cy

                # Length Reduction
                if self.currentLength > self.allowedLength:
                    for i, length in enumerate(self.lengths):
                        self.currentLength -= length

                        self.lengths.pop(i)
                        self.points.pop(i)

                        if self.currentLength < self.allowedLength:
                            break

                # check if snake ate the food
                rx, ry = self.foodPoint
                if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and ry - self.hFood // 2 < cy + self.hFood:
                    self.randomFoodLocation()
                    self.allowedLength += 10
                    self.score += 1

                # Draw snake
                if self.points:
                    for i, point in enumerate(self.points):
                        if i != 0:
                            cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                    cv2.circle(img, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

                # Draw food
                rx, ry = self.foodPoint
                imgMain = cvzone.overlayPNG(imgMain, self.imgFood,
                                            (rx - self.wFood // 2, ry - self.hFood // 2))
                cvzone.putTextRect(imgMain, f"Your score: {self.score}", (50, 80), 3, 3, 10)

                # check for collision
                pts = np.array(self.points[:-4], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
                minDistance = cv2.pointPolygonTest(pts, (cx, cy), True)

                if -0.3 <= minDistance <= 0.3 and self.currentLength > 200:
                    # When everything done, release
                    cap.release()
                    cv2.destroyAllWindows()



            return imgMain

    game = SnakeGameClass(r"Games/SnakeGame/Donut.png")

    while True:
        success, img = cap.read()
        if img is None:
            cap.release()
            cv2.destroyAllWindows()
            try:
                loading("audio/spinball1.mp3", "photos_GUI/last.gif", 6000, 28, 45)

            except:
                pass


            cap.release()
            cv2.destroyAllWindows()
            return
        else:
            img = cv2.flip(img, 1)

            hands, img = detector.findHands(img, flipType=False)

            if hands:
                lmList = hands[0]['lmList']
                pointIndex = lmList[8][:2]
                img = game.update(img, pointIndex)

            cv2.imshow("Image", img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                game.gameOver = False
                game.score = 0
                cap.release()
                cv2.destroyAllWindows()
                return
