# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 08:25:01 2025

@author: Nishu
"""

import speech_recognition as sr
AUDIO_FILE=("try.wav")

#use audio file as the source 

r=sr.Recognizer()  #initilize the reconizer

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
    #reads audio file
    
try:
    print("audio file contains: "+r.recognize_google(audio))
    
except sr.UnknownValueError:
    print("Google speech recognization could not understand audio")
except sr.RequestError:
    print("Couldn't get result from google speech rechonization")
    
    