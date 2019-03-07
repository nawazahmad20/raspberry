import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set the mode to broadcomm
GPIO.cleanup()

#choose the GPIO pin
fwd1 = 23  # pin 16
#yellow = 22 # pin15

# declare selected pin as output pin
GPIO.setup(fwd1, GPIO.OUT)
#GPIO.setup(yellow, GPIO.OUT)

sleep_time = .2


def forward():
  GPIO.output(fwd1, GPIO.HIGH)
  #GPIO.output(yellow, GPIO.LOW)
  #time.sleep(sleep_time)

def stop():
  GPIO.output(fwd1, GPIO.LOW)
  #GPIO.output(yellow, GPIO.HIGH)
  #time.sleep(sleep_time)


GPIO.cleanup()
