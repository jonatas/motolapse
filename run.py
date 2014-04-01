import RPi.GPIO as GPIO
import picamera

execfile("motor.py")

GPIO.setmode(GPIO.BCM)

PINS_ON_ULN = [17,18,23,22]
ROTATION_ANGLE = 180
PICTURE_EACH_HOW_MUCH_DEGREES = 5

motor = Motor(PINS_ON_ULN)
motor.rpm = 1
with picamera.PiCamera() as camera:
    degree = 0
    while degree < ROTATION_ANGLE:
        filename = 'deg'+str(degree)+'.jpg'
        print "Capturing: " + filename
        camera.capture(filename)
	degree += PICTURE_EACH_HOW_MUCH_DEGREES 
	print "move to "+str(degree)
        motor.move_to(degree)
