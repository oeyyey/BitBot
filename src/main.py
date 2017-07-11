# !/usr/bin/python
import random
from subprocess import PIPE, Popen
import os
import bitbot_ai
import snowboydecoder

models = ["resources/BitBot.pmdl"]

ans_list = ["น้อมรับคำสั่ง", "ว่ายังไงจ๊ะ", "มาแล้วจ้า", "มีอะไรให้รับใช้",
            "ขอโทษจ้าฉันมาแล้ว", "มาแล้ว มาแล้ว", "มีอะไรขอให้บอก", "เรียกฉันหรอ"]

def bitbot():
    detector.terminate()
    print("Conversation Started")
    bitbot_ai.main(True)
    print("Conversation Stop")
    print("Listening")
    global detector
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1.2)
    detector.start(callbacks)

callbacks = [bitbot]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1.2)
print("Listening")
detector.start(detected_callback=callbacks)
