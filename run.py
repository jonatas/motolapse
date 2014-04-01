
import RPi.GPIO as GPIO
import picamera
execfile("motor.py")
with picamera.PiCamera() as camera:
    GPIO.setmode(GPIO.BCM)
    m = Motor([17,18,23,22])
    m.rpm = 1
    print "Pause in seconds: " + `m._T`
    m.move_to(90)
    m.move_to(90)
    camera.capture('deg90.jpg')
    sleep(1)
    m.move_to(180)
    camera.capture('180deg.jpg')
    sleep(1)
    m.move_to(270)
    camera.capture('270deg.jpg')
    sleep(1)
    m.move_to(360)
    camera.capture('360deg.jpg')
    GPIO.cleanup()
