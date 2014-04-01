motolapse
=========

Rotative timelapse experiments using raspberry pi, the official pi cam, a ULN2003 and a 28BYJ-48 motor

## configure

Search and exchange the 3 variables to work with your needs,

### Configure the ULN2003 pins

Change the pins on the following line to configure your own motors. The four respective values is ordered by 1N1,1N2,1N3,1N4.

```python
PINS_ON_ULN = [17,18,23,22]
```
### How much do you want to rotate?

```python
ROTATION_ANGLE = 180
```
### How much pictures?

Configure the degrees per picture taken.

```python
PICTURE_EACH_HOW_MUCH_DEGREES = 5
```



# Run it!

After all run it using:

`sudo python run.py`

# References and codes

* http://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
* http://blog.scphillips.com/2012/12/a-python-class-to-move-the-stepper-motor/
* http://pypi.python.org/pypi/picamera/
* http://www.tutorialspoint.com/python/python_while_loop.htm

