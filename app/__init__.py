from flask import Flask
from config import Config
import RPi.GPIO as GPIO

app = Flask(__name__)
app.config.from_object(Config)
GPIO.setmode(GPIO.BCM)


from app import api, routes