from app import app
import RPi.GPIO as GPIO

green_light = app.config["GREEN_LED"]
yellow_light = app.config["YELLOW_LED"]
red_light = app.config["RED_LED"]
GPIO.setmode(GPIO.BCM)
print(type(green_light))
GPIO.setup(green_light, GPIO.OUT)
GPIO.setup(yellow_light, GPIO.OUT)
GPIO.setup(red_light, GPIO.OUT)

@app.route('/color/green')
def green():
    print("Turning on GREEN light")
    print("GREEN is on port {0}".format(green_light))
    GPIO.output(green_light, GPIO.HIGH)
    GPIO.output(yellow_light, GPIO.LOW)
    GPIO.output(red_light, GPIO.LOW)

@app.route('/color/red')
def red():
    print("Turning on RED light")
    print("RED is on port {0}".format(red_light))
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)

@app.route('/color/yellow')
def yellow():
    print("Turning on YELLOW light")
    print("YELLOW is on port {0}".format(yellow_light))
    GPIO.output(green_light, GPIO.LOW)
    GPIO.output(yellow_light, GPIO.HIGH)
    GPIO.output(red_light, GPIO.LOW)
