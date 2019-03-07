import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set the mode to broadcomm
GPIO.cleanup()

#choose the GPIO pins
fwd1 = 23  # pin 16
bwd1 = 24 #pin 18
fwd2 = 16 # pin 36
bwd2 = 20 # pin 38

# declare selected pin as output pin
GPIO.setup(fwd1, GPIO.OUT)
GPIO.setup(bwd1, GPIO.OUT)
GPIO.setup(fwd2, GPIO.OUT)
GPIO.setup(bwd2, GPIO.OUT)

sleep_time = .2


def forward():
  GPIO.output(fwd1, GPIO.HIGH)
  GPIO.output(bwd1, GPIO.LOW)
  GPIO.output(fwd2, GPIO.HIGH)
  GPIO.output(bwd2, GPIO.LOW)

def backward():
  GPIO.output(fwd1, GPIO.LOW)
  GPIO.output(bwd1, GPIO.HIGH)
  GPIO.output(fwd2, GPIO.LOW)
  GPIO.output(bwd2, GPIO.HIGH)

def left():
  GPIO.output(fwd1, GPIO.HIGH)
  GPIO.output(bwd1, GPIO.LOW)
  GPIO.output(fwd2, GPIO.LOW)
  GPIO.output(bwd2, GPIO.HIGH)

def right():
  GPIO.output(fwd1, GPIO.LOW)
  GPIO.output(bwd1, GPIO.HIGH)
  GPIO.output(fwd2, GPIO.HIGH)
  GPIO.output(bwd2, GPIO.LOW)

def stop():
  GPIO.output(fwd1, GPIO.LOW)
  GPIO.output(bwd1, GPIO.LOW)
  GPIO.output(fwd2, GPIO.LOW)
  GPIO.output(bwd2, GPIO.LOW)


