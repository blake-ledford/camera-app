#this is the script that plays videos
import numpy as numpy
import cv2
import subprocess
import os
import sys

#set camera properties
set_height = 560
set_width = 860
set_fps = 20

#closes the x11 session so the terminal will return to normal
def stop_x11_session():
    try:
        subprocess.run(['killall', 'xinit'], check=True)
        print("stopped session")

    except subprocess.CalledProcessError as e:
        print(f"Error stopping x11 session: {e}")

#this function sets the props of the camera and returns a camera instance
def set_a_camera_instance(path, index):

    if os.path.exists(path):    
        camera_instance = cv2.VideoCapture(index)
        camera_instance.set(cv2.CAP_PROP_FRAME_HEIGHT, set_height)
        camera_instance.set(cv2.CAP_PROP_FRAME_WIDTH, set_width)
        camera_instance.set(cv2.CAP_PROP_FPS, set_fps)
        return camera_instance
    else:
        print("could not find camera isntance")


#camera instance declarations
camera_instance0 = set_a_camera_instance("/dev/video0", 0)
if not camera_instance0.isOpened():
    print("Error: could not open camera0 during instance declaration")
    exit()

# #camera instance declarations
# camera_instance2 = set_a_camera_instance("/dev/video2", 2)
# if not camera_instance0.isOpened():
#     print("Error: could not open camera0 during instance declaration")
#     exit()

# #camera instance declarations
# camera_instance4 = set_a_camera_instance("/dev/video4", 4)
# if not camera_instance0.isOpened():
#     print("Error: could not open camera0 during instance declaration")
#     exit()

# #camera instance declarations
# camera_instance6 = set_a_camera_instance("/dev/video6", 6)
# if not camera_instance0.isOpened():
#     print("Error: could not open camera0 during instance declaration")
#     exit()

#loop that plays the camera images
while True:
    #text default values
    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
    fontScale = 1  # Font size
    color = (0, 255, 0)  # Text color (B, G, R) - here, blue
    thickness = 2  # Line thickness of the text
    lineType = cv2.LINE_AA  # Anti-aliasing for smoother text edge
    org = (315, 30)

    #camera 0 
    ret, frame = camera_instance0.read()
    window_name = "Camera 1"
    cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    cv2.moveWindow(window_name, 10,10)
    #define text
    cv2.putText(frame, window_name, org, font, fontScale, color, thickness, lineType)
    #resized_frame0 = cv2.resize(frame, (set_width, set_height), interpolation=cv2.INTER_LINEAR)
    cv2.imshow(window_name, frame)

    #camera 2
    ret, frame = camera_instance0.read()
    window_name = "Camera 2"
    cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    cv2.moveWindow(window_name, 420,10)
    #define text
    cv2.putText(frame, window_name, org, font, fontScale, color, thickness, lineType)
    #resized_frame2 = cv2.resize(frame, (set_width, set_height), interpolation=cv2.INTER_LINEAR)
    cv2.imshow(window_name, frame)

    #camera 4
    ret, frame = camera_instance0.read()
    window_name = "Camera 3"
    cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    cv2.moveWindow(window_name, 10, 365)
    #define text
    cv2.putText(frame, window_name, org, font, fontScale, color, thickness, lineType)
    #resized_frame4 = cv2.resize(frame, (set_width, set_height), interpolation=cv2.INTER_LINEAR)
    cv2.imshow(window_name, frame)

    #camera 6
    ret, frame = camera_instance0.read()
    window_name = "Camera 4"
    cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    cv2.moveWindow(window_name, 420,365)
    #define text
    cv2.putText(frame, window_name, org, font, fontScale, color, thickness, lineType)
    #resized_frame6 = cv2.resize(frame, (set_width, set_height), interpolation=cv2.INTER_LINEAR)
    cv2.imshow(window_name, frame)

    # #camera 8
    # ret, frame = camera_instance0.read()
    # window_name = "Camera 5"
    # cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    # cv2.moveWindow(window_name, 10,700)
    # #define text
    # cv2.putText(frame, window_name, org, font, fontScale, color, thickness, lineType)
    # cv2.imshow(window_name, frame)

    # #camera 10
    # ret, frame = camera_instance0.read()
    # window_name = "Camera 6"
    # cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    # cv2.moveWindow(window_name, 420,700)
    # #define text
    # cv2.putText(frame, window_name, org, font, fontScale, color, thickness, lineType)
    # cv2.imshow(window_name, frame)
    
    #press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

#releases assets and kills sessions
camera_instance0.release()
cv2.destroyAllWindows() 
stop_x11_session()
