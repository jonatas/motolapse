
import RPi.GPIO as GPIO
import picamera
execfile("motor.py")
with picamera.PiCamera() as camera:
    GPIO.setmode(GPIO.BCM)
    m = Motor([17,18,23,22])
    m.rpm = 1
    print "ok intialized"
    degree = 0
    rotationAngle = 180
    rotationStep = 5
    camera.capture('deg0.jpg')
    while degree < rotationAngle:
	degree += rotationStep 
	print "move to "+str(degree)
        m.move_to(degree)
        filename = 'deg'+str(degree)+'.jpg'
        print "Capturing: " + filename
        camera.capture(filename)
