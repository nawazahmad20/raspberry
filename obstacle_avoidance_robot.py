import RPi.GPIO as GPIO
import time
#import motor_control as mc

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# define the GPIO pins for trigger and echo
TRIG = 17 # pin 11
ECHO = 22 # pin 15
fwd1 = 23 # pin 18

# define the pins as input/output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(fwd1, GPIO.OUT)
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
  return distance

while True:
  distance = get_distance()
  if distance < 10:
   GPIO.output(fwd1, GPIO.LOW)
  else:
    GPIO.output(fwd1, GPIO.HIGH)
  time.sleep(.1)

GPIO.cleanup()
