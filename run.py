import RPi.GPIO as GPIO
import picamera
from time import sleep
from motor import Motor

GPIO.setmode(GPIO.BCM)

PINS_ON_ULN = [17,18,22,23]
ROTATION_ANGLE = 225
PICTURE_EACH_HOW_MUCH_DEGREES = 1
MILLISECONDS_OF_WORK = 4 * 60 * 60 * 1000
STEPS = ROTATION_ANGLE / PICTURE_EACH_HOW_MUCH_DEGREES
SLEEP_PER_STEP = MILLISECONDS_OF_WORK / STEPS
SLEEP_PER_PICTURE = 10000

print "Sleep per step: " + str(SLEEP_PER_STEP)
motor = Motor(PINS_ON_ULN)
motor.rpm = 1
with picamera.PiCamera() as camera:
    degree = 0.0
    while degree < ROTATION_ANGLE:
        filename = 'deg'+str(degree)+'.jpg'
        print "Capturing: " + filename
        camera.capture(filename)
	degree += PICTURE_EACH_HOW_MUCH_DEGREES 
	print "move to "+str(degree)
        motor.move_to(degree)
	sleep(SLEEP_PER_STEP)
