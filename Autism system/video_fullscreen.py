import cv2
from ffpyplayer.player import MediaPlayer


def fullscreen(name_file):
    cap = cv2.VideoCapture(f"{name_file}")
    player = MediaPlayer(f"{name_file}")

    
    if (cap.isOpened() == False):
        print("Error opening video  file")
    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        if ret == True:
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("window", frame)

            if val != 'eof' and audio_frame is not None:
                # audio
                img, t = audio_frame

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):

                break
        # Break the loop
        else:
            break

        # When everything done, release
    player.close_player()
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()

