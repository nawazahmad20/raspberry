import RPi.GPIO as GPIO
import time
import motor_control as mc
import get_distance as gd
import sys

GPIO.setmode(GPIO.BCM)

# define the GPIO pins for trigger and echo
TRIG = 17 # pin 11
ECHO = 22 # pin 15

# define the pins as input/output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

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


if __name__ == "__main__":
  try:
    prev_values = [0,0,0,0,0]
    while True:
      prev_values, distance = gd.get_distance(prev_values)
      if distance <= 4:
        mc.backward()
        time.sleep(2)
        mc.right()
        time.sleep(.5)
      else:
        mc.forward()
      time.sleep(.1)
  except KeyboardInterrupt:
    mc.stop()
    GPIO.cleanup()
    sys.exit()

