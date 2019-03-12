# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import time
import RPi.GPIO as GPIO
import sys

from picamera.array import PiRGBArray
from picamera import PiCamera
import motor_control as mc

GPIO.setmode(GPIO.BCM)


#choose the GPIO pins for mptor control
fwd1 = 23  # pin 16
bwd1 = 24 #pin 18
fwd2 = 16 # pin 36
bwd2 = 20 # pin 38

# declare selected pin as output pin
GPIO.setup(fwd1, GPIO.OUT)
GPIO.setup(bwd1, GPIO.OUT)
GPIO.setup(fwd2, GPIO.OUT)
GPIO.setup(bwd2, GPIO.OUT)

model = load_model("model")


def control_robot(image):
    prediction = np.argmax(model.predict(image))
    print(model.predict(image))
    print(prediction)
    if prediction == 0:
        print("forward")
        mc.forward()
    elif prediction == 2:
        print("left")
        mc.left()
    else:
        print("right")
        mc.right()


if __name__ == "__main__":
    try:
        mc.stop()
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))

        # allow the camera to warmup
        time.sleep(0.1)

        # capture frames from the camera
        start = 1

        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
          # grab the raw NumPy array representing the image, then initialize the timestamp
          # and occupied/unoccupied text
          image = frame.array
          # show the frame
          key = cv2.waitKey(1) & 0xFF
          #cv2.imwrite(str(start) + ".jpg", image)
          #start = start + 1

          image = cv2.resize(image, (28, 28))
          image = img_to_array(image)
          image = np.array(image, dtype="float") / 255.0
          image = image.reshape(-1, 28, 28, 3)
          #cv2.imshow("Frame", image[0])

          control_robot(image)

          # clear the stream in preparation for the next frame
          rawCapture.truncate(0)

          # if the `q` key was pressed, break from the loop
          if key == ord("q"):
            break
          time.sleep(.1)

    except KeyboardInterrupt:
        mc.stop()
        GPIO.cleanup()
        sys.exit()
