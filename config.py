import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    green_led = os.environ.get('TL_GREEN_LED') or 21
    yellow_led = os.environ.get('TL_YELLOW_LED') or 20
    red_led = os.environ.get('TL_RED_LED') or 16