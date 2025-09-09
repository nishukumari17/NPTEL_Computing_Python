# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 08:34:36 2025

@author: Nishu
"""

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")