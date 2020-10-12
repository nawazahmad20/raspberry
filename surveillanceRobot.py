import os
import multiprocessing
from multiprocessing import Pool
import time
import RPi.GPIO as GPIO
import Utils.motor_control as mc
#from picamera.array import PiRGBArray
#from picamera import PiCamera
#import cv2
import sys
import readchar
import curses

GPIO.setmode(GPIO.BCM)

#choose the GPIO pins for motor control
fwd1 = 23  # pin 16
bwd1 = 24  # pin 18
fwd2 = 16  # pin 36
bwd2 = 20  # pin 38

# declare selected pin as output pin
GPIO.setup(fwd1, GPIO.OUT)
GPIO.setup(bwd1, GPIO.OUT)
GPIO.setup(fwd2, GPIO.OUT)
GPIO.setup(bwd2, GPIO.OUT)

# function to control direction of motors/robot based on pressed key
def movementOnKeyPress(key):
  if key == 'w':
    mc.forward()
  elif key == 's':
    mc.backward()
  elif key == 'd':
    mc.left()
  elif key == 'a':
    mc.right()
  elif key == " ":
    mc.stop()
  else:
    mc.stop()

# function to display images from raspberry pi camera
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
    rawCapture.truncate(0)


# function to get the key pressed on keyboard
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
      movementOnKeyPress(str(key)) # move the robot based on input key
      if key == os.linesep:
        break
    except Exception as e:
      #No input
      pass

# function to run processes in multiprocessing
def run_process(process):
  try:
    process()
  except:
    curses.wrapper(main)


if __name__ == "__main__":
  try:
    #processes = (cameradisplay, main)
    #pool = Pool(processes=2)
    processes = [main]
    pool = Pool(processes=1)
    pool.map(run_process, processes) # run both the processes in parallel
  except KeyboardInterrupt:
    mc.stop() # stop rotation of motors during termination of script
    GPIO.cleanup()
    sys.exit()
