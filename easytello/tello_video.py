import cv2

def video_process(stream_state, tello_ip):
    # Creating stream capture object
    cap = cv2.VideoCapture('udp://'+tello_ip+':11111')
    # Runs while 'stream_state' is True
    while stream_state.value == 1:
        ret, frame = cap.read()
        cv2.imshow('DJI Tello', frame)

        # Video Stream is closed if escape key is pressed
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()