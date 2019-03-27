from app import app
import RPi.GPIO as GPIO

green_light = app.config["green_led"]
yellow_light = app.config["yellow_led"]
red_light = app.config["red_led"]

@app.route('/color/green')
def green():
    GPIO.output(green_light, GPIO.HIGH)
    GPIO.output(yellow_light, GPIO.LOW)
    GPIO.output(red_light, GPIO.LOW)

@app.route('/color/red')
def red():
    GPIO.output(green_light, GPIO.LOW)
    GPIO.output(yellow_light, GPIO.LOW)
    GPIO.output(red_light, GPIO.HIGH)

@app.route('/color/yellow')
def yellow():
    GPIO.output(green_light, GPIO.LOW)
    GPIO.output(yellow_light, GPIO.HIGH)
    GPIO.output(red_light, GPIO.LOW)
