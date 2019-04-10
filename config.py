import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    GREEN_LED = os.environ.get("TL_GREEN_LED") or 21
    YELLOW_LED = os.environ.get("TL_YELLOW_LED") or 20
    RED_LED = os.environ.get("TL_RED_LED") or 16
