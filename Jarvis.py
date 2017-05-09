#JARVIS
from pprint import pprint
import methods
import time
import win32gui
import win32api
import win32con
import apiai
import winshell
import subprocess
import os
import inspect
import speech_recognition as sr

CLIENT_ACCESS_TOKEN = '8c564ca4f1ae4c45acea584bc16116b5'

ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
request = ai.text_request()
request.lang = 'en'
request.session_id = 'user_id_lelo'

# found = methods.findWindowWithTitle("Untitled - Notepad")
# pprint(found)

# handle = methods.getWindowWithTitle("untitled - notepad")
# monHandle = win32api.MonitorFromWindow(handle)
# print(win32api.GetMonitorInfo(monHandle))


# this is called from the background thread
def callback(recognizer, audio):
    print("-------------")
    try:
        print("DEBUG: recognizing..")
        recognizedText = r.recognize_google(audio)
        print(">> " + recognizedText)
    except:
        print('DEBUG: Error audio')
        return
    try:
        print("DEBUG: requesting..")
        request.query = recognizedText
        response = request.getresponse()
        pprint(response.read())
    except:
        print("Error getting response")


# obtain audio from the microphone
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print("Say something: ")
    r.adjust_for_ambient_noise(source, duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# main loop
while True:
    time.sleep(0.1)