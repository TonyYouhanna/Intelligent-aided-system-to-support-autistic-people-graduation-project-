import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import cv2
import numpy as np
import time


def read_face():
    face_classifier = cv2.CascadeClassifier("Expression/face.xml")  # xml file for OpenCV to detect frontal face
    model = load_model("Expression/checkpoint1.h5")  # out pretrained weighted file

    class_labels = ["Angry", "Happy", "Neutral", "Sad", "Surprise"]

    cap = cv2.VideoCapture(0)  # your video file here ("0" in case of webcam)

    try:
        counter = [0, 0, 0, 0, 0]
        while True:
            ret, frame = cap.read()  # return value and the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # converting to gray as our data was trained using gray images

            faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 225), 3)  # drawing the rectangle over faces

                roi_gray = gray[y:y + h, x:x + w]
                roi_gray = cv2.resize(roi_gray, (48, 48),
                                      interpolation=cv2.INTER_AREA)  # resizing as per our dataset 48*48

                if np.sum([roi_gray]) != 0:
                    roi = roi_gray.astype("float") / 255.0
                    roi = tf.keras.preprocessing.image.img_to_array(roi)
                    roi = np.expand_dims(roi, axis=0)
                    pred = model.predict(roi)[0]
                    labels = class_labels[pred.argmax()]

                    if labels == "Happy":
                        counter[0] = counter[0] + 1
                    elif labels == "Neutral":
                        counter[1] = counter[1] + 1

                    elif labels == "Angry":
                        counter[2] = counter[2] + 1
                    elif labels == "Surprise":
                        counter[3] = counter[3] + 1
                    elif labels == "Sad":
                        counter[4] = counter[4] + 1

                    max_value = max(counter)
                    if max_value == 40:
                        print("we got you")
                        max_index = counter.index(max_value)
                        if max_index == 0:
                            print('We are glad you are happy')
                            print(counter)
                            counter = [0, 0, 0, 0]
                            cap.release()
                            cv2.destroyAllWindows()
                            return max_index
                        elif max_index == 1:
                            print('Please move your face and try to interact with us')
                            print(counter)
                            counter = [0, 0, 0, 0]
                            cap.release()
                            cv2.destroyAllWindows()
                            return max_index
                        elif max_index == 2:
                            print('We aim that you wont be angry ')
                            print(counter)
                            counter = [0, 0, 0, 0]
                            cap.release()
                            cv2.destroyAllWindows()
                            return max_index
                        elif max_index == 3:
                            print('why are you surprised ')
                            print(counter)
                            counter = [0, 0, 0, 0]
                            cap.release()
                            cv2.destroyAllWindows()
                            return max_index

                        elif max_index == 4:
                            print('Why are you so sad? ')
                            print(counter)
                            counter = [0, 0, 0, 0]
                            cap.release()
                            cv2.destroyAllWindows()
                            return max_index

                    # gets the label from our array
                    label_position = (x, y)
                    # starting of our rectangle
                    cv2.putText(frame, labels, label_position, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 225, 0), 3)
                    # places the text




                else:
                    cv2.putText(frame, "No Face Found Sorry!", (20, 60), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, "red", 3)

            cv2.namedWindow('Facial Expression Recognition', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Facial Expression Recognition', 1000, 800)
            cv2.imshow("Facial Expression Recognition", frame)
            # showing the final rendered video
            if cv2.waitKey(1) & 0xFF == ord("q"):  # if "Q" is pressed then the video window will be closed
                break
        cap.release()
        cv2.destroyAllWindows()
        # closes the frame window
    except:
        print("error occurred")
        cap.release()
        cv2.destroyAllWindows()


counter = [0, 0, 0, 0, 0]
# read_face()
