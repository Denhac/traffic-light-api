from app import app
import RPi.GPIO as GPIO

green_light = app.config["GREEN_LED"]
yellow_light = app.config["YELLOW_LED"]
red_light = app.config["RED_LED"]

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
    GPIO.output(green_light, GPIO.LOW)
    GPIO.output(yellow_light, GPIO.LOW)
    GPIO.output(red_light, GPIO.HIGH)

@app.route('/color/yellow')
def yellow():
    print("Turning on YELLOW light")
    print("YELLOW is on port {0}".format(yellow_light))
    GPIO.output(green_light, GPIO.LOW)
    GPIO.output(yellow_light, GPIO.HIGH)
    GPIO.output(red_light, GPIO.LOW)
