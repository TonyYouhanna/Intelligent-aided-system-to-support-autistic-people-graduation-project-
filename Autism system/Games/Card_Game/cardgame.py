import numpy as np
import cv2
import random

import time
import os
import sys
from TalkFunction import *
from loadingfun import *

def card_game():

    try:
        loading("audio/card1.mp3", "photos_GUI/last.gif", 6000, 28, 45)

    except:
        pass


    x = game_start(0)
    if x == 1:
        return

def game_start(count):
    cap = cv2.VideoCapture(0)
    whT = 320
    confThreshold = 0.5
    nms_threshold = 0.3
    classesFile = 'Games/Card_Game/coco.names'
    classNames = []

    with open(classesFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
        rand = random.choice(
            ['teddy bear', 'dog', 'horse', 'cup', 'sheep', 'zebra', 'apple', 'clock', 'bird', 'cat', 'orange', 'vase',
             'bear', 'elephant', 'bus', 'cell phone', 'scissors', 'train', 'cow'])
        print(rand)
        print(classNames.index(rand))
        value = classNames.index(rand)
        start_time = time.time()

        talk(f"choose the one that contain {rand} ", "audio/file.mp3", 4)
        os.remove("audio/file.mp3")

        try:
            loading("audio/card1.mp3", "photos_GUI/zebra.jpeg", 6000, 28, 45)

        except:
            pass


    modelConfiguration = 'Games/Card_Game/yolov3-tiny.cfg'
    modelWeights = 'Games/Card_Game/yolov3-tiny.weights'
    net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def findObjects(outputs, img, value, start_time) -> object:
        hT, wT, cT = img.shape
        bbox = []
        num = 0
        classIds = []
        confs = []
        names = ["good jop", "fantastic", "you are very smart", "that is correct", "i'm proud of you",
                 "keep up the good work", "excellent", "you are the best"]

        for output in outputs:
            end_time = time.time()

            for det in output:

                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold:
                    w, h = int(det[2] * wT), int(det[3] * hT)
                    x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))
                    if classId == value:

                        call = random.choice(names)
                        talk(call, "audio/file.mp3", 3)
                        os.remove("audio/file.mp3")
                        return 1

                elapsed = end_time - start_time
                if elapsed >=20 :

                    try:
                        loading("audio/card2.mp3", "photos_GUI/last.gif", 6000, 28, 45)

                    except:
                        pass
                    return 0




            indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nms_threshold)

            for i in indices:
                box = bbox[i]
                x, y, w, h = box[0], box[1], box[2], box[3]
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%', (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

    while True:
        success, img = cap.read()
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        layerNames = net.getLayerNames()
        outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]
        outputs = net.forward(outputNames)
        val = findObjects(outputs, img, value, start_time)
        if val == 0:
            cap.release()
            cv2.destroyAllWindows()
            game_start(count)
        if val == 1:
            count = count + 1

            if count >= 5:
                try:
                    loading("audio/card3.mp3", "photos_GUI/last.gif", 6000, 28, 45)

                except:
                    pass
                quit()
            game_start(count)
    cap.release()
    cv2.destroyAllWindows()


