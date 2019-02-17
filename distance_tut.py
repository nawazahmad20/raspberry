import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# define the GPIO pins for trigger and echo
TRIG = 17 # pin 11
ECHO = 22 # pin 15

# define the pins as input/output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_distance():
  GPIO.output(TRIG, True)
  time.sleep(.0001)
  GPIO.output(TRIG, False)
  while GPIO.input(ECHO) == False:
    start = time.time()
  while GPIO.input(ECHO) == True:
    end = time.time()
  try:
    sig_time = end - start
    distance = sig_time /0.000058
    print(" Distance is {} cm".format(distance))
  except:
    distance = 1000
    print("object far away")

while True:
  get_distance()
  time.sleep(.1)

GPIO.cleanup()
