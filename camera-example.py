import picamera
import time

camera = picamera.PiCamera()
camera.vflip = True
#camera.capture('test.jpg')
camera.start_recording('example_vid.h264')
time.sleep(10)
camera.stop_recording()
