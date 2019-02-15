import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

out = 17

GPIO.setup(out, GPIO.OUT)

GPIO.output(out, GPIO.HIGH)
time.sleep(1)
GPIO.output(out, GPIO.LOW)
time.sleep(1)
GPIO.output(out, GPIO.HIGH)
time.sleep(1)
GPIO.output(out, GPIO.LOW)
time.sleep(1)
GPIO.output(out, GPIO.HIGH)
time.sleep(1)
GPIO.output(out, GPIO.LOW)
GPIO.cleanup()
