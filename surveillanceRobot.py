import os
import multiprocessing
from multiprocessing import Pool
import time
import RPi.GPIO as GPIO
import Utils.motor_control as mc
import Utils.keydetection as kd
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import sys
import readchar

import curses
import os

GPIO.setmode(GPIO.BCM)

# define the GPIO pins for trigger and echo
TRIG = 17 # pin 11
ECHO = 22 # pin 15

# define the pins as input/output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#choose the GPIO pins for mptor control
fwd1 = 23  # pin 16
bwd1 = 24  # pin 18
fwd2 = 16  # pin 36
bwd2 = 20  # pin 38

# declare selected pin as output pin
GPIO.setup(fwd1, GPIO.OUT)
GPIO.setup(bwd1, GPIO.OUT)
GPIO.setup(fwd2, GPIO.OUT)
GPIO.setup(bwd2, GPIO.OUT)

key_global = None

def movementOnKeyPress(key):
  #global key_global
  #key =  key_global
  print(key)
  if key == 'w':
    mc.forward()
  elif key == 's':
    mc.backward()
  elif key == 'a':
    mc.left()
  elif key == 'd':
    mc.right()
  elif key == " ":
    mc.stop()
  else:
  #time.sleep(.1)
    mc.stop()


def cameradisplay():
  # initialize the camera and grab a reference to the raw camera capture
  camera = PiCamera()
  camera.resolution = (640, 480)
  camera.framerate = 32
  rawCapture = PiRGBArray(camera, size=(640, 480))
  # allow the camera to warmup
  time.sleep(0.5)

  for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    #image = cv2.resize(image, (28, 28))
    #image = img_to_array(image)
    #image = np.array(image, dtype="float") / 255.0
    #image = image.reshape(-1, 28, 28, 3)
    #cv2.imshow("Frame", image[0])
    #movementOnKeyPress(key)
    rawCapture.truncate(0)
    #time.sleep(.5)


def main(win):
    global key_global
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
           key = win.getkey()
           win.clear()
           win.addstr("Detected key:")
           win.addstr(str(key))
           movementOnKeyPress(str(key))
           #key_global = key
           if key == os.linesep:
              break
        except Exception as e:
           # No input
           pass


def run_process(process):
  try:
    process()
  except:
    curses.wrapper(main)


if __name__ == "__main__":
  try:
    processes = (cameradisplay, main,  movementOnKeyPress)
    pool = Pool(processes=2)
    pool.map(run_process, processes)

  except KeyboardInterrupt:
    mc.stop()
    GPIO.cleanup()
    sys.exit()
