import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set the mode to broadcomm
GPIO.cleanup()

#choose the GPIO pin
red = 17  # pin 11
yellow = 22 # pin15

# declare selected pin as output pin
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

sleep_time = .2

for i in range(15):
  GPIO.output(red, GPIO.HIGH)
  GPIO.output(yellow, GPIO.LOW)
  time.sleep(sleep_time)
  GPIO.output(red, GPIO.LOW)
  GPIO.output(yellow, GPIO.HIGH)
  time.sleep(sleep_time)

GPIO.cleanup()
