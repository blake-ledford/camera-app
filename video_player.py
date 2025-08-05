#this is the script that plays videos
import numpy as numpy
import cv2
import subprocess
import os
import sys

#arguement vars
passed_source = ""
passed_index = 0
converted_index = 0
local_check = "/dev/video"

#set camera properties
set_height = 560
set_width = 860
set_fps = 30

if len(sys.argv) > 1:
    print(f"argument passed: {sys.argv[1]}")
    passed_source = sys.argv[1]
    passed_index = sys.argv[2]
    converted_index = int(passed_index)
else:
    print("received no arguments")

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

#this function sets the props of the camera and returns a camera instance
def set_rtsp_instance(path):

    camera_instance = cv2.VideoCapture(path)
    camera_instance.set(cv2.CAP_PROP_FRAME_HEIGHT, set_height)
    camera_instance.set(cv2.CAP_PROP_FRAME_WIDTH, set_width)
    camera_instance.set(cv2.CAP_PROP_FPS, set_fps)
    return camera_instance

#determine local source or url
if local_check in passed_source:
    print("the source is local")
    camera_instance0 = set_a_camera_instance(passed_source, converted_index)
else:
    print("the source is a url")
    camera_instance0 = set_rtsp_instance(passed_source)

#camera instance declarations
#camera_instance0 = set_a_camera_instance(passed_source, converted_index)
if not camera_instance0.isOpened():
    print("Error: could not open camera0 during instance declaration")
    exit()

#loop that plays the camera images
while True:
    #text default values
    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
    fontScale = 1  # Font size
    color = (0, 255, 0)  # Text color (B, G, R) - here, blue
    thickness = 2  # Line thickness of the text
    lineType = cv2.LINE_AA  # Anti-aliasing for smoother text edge
    org = (315, 30)  # Bottom-left corner of the text (x, y)

    #camera instance
    ret, frame = camera_instance0.read()
    window_name = "Camera " + passed_index
    cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
    cv2.moveWindow(window_name, 10,10)
    #define text
    cv2.putText(frame, window_name, org, font, fontScale, color, thickness, lineType)
    #Attempt to resize
    resized_frame = cv2.resize(frame, (set_width, set_height), interpolation=cv2.INTER_LINEAR)
    cv2.imshow(window_name, resized_frame)
    #cv2.imshow(window_name, frame) 

    #press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

#releases assets and kills sessions
camera_instance0.release()
cv2.destroyAllWindows() 
stop_x11_session()
