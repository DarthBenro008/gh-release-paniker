from typing import Optional
from fastapi import FastAPI
app = FastAPI()


import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

LED=21
BUZZER=23

GPIO.setup(LED,GPIO.OUT) 

def panikMode():
    print("Entering PanikMode")
    GPIO.output(LED,GPIO.HIGH)
    GPIO.output(BUZZER,GPIO.HIGH)


def stopPanikMode():
    print("Exiting PanikMode")
    GPIO.output(LED,GPIO.LOW)
    GPIO.output(BUZZER,GPIO.LOW)

@app.get("/")
def read_root():
    return {"ping": "pong"}


@app.get("/stop")
def stopPanik():
    stopPanik()
    return {"paniking": "false"}

@app.get("/panik")
def panik():
    panikMode()
    return {"paniking": True}