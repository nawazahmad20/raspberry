from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# define the GPIO pins for trigger and echo
DIR = 17 # pin 11
STEP = 22 # pin 15
CW = 1
CCW = 0
SPR = 200



# define the pins as input/output
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)

step_count = SPR *2
delay = .00208

for x in range(step_count):
  GPIO.output(STEP, GPIO.HIGH)
  sleep(delay)
  GPIO.output(STEP, GPIO.LOW)
  sleep(delay)
