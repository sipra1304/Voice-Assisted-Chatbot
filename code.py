from __future__ import print_function
import speech_recognition as sr
import os
import time
from gtts import gTTS
import datetime
import pyjokes
import warnings
import webbrowser
import calendar
import pyttsx3
import random
import smtplib
import playsound
#import wolframalpha
import requests
import json
##import winshell
import subprocess
#from twilio.rest import Client
import pickle
import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
from selenium import webdriver
from time import sleep
from googletrans import Translator
import streamlit as st

warnings.filterwarnings("ignore")
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def hin_eng():
    recog=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say english / hindi :")
        audio=recog.listen(source, timeout=10)
    lang=""
    try:
        lang=recog.recognize_google(audio)
        if lang.lower()=='english':
            data=True
        else: 
            data=False
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)
    return data    
        
def rec_audio():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        st.write("Listening...")
        recog.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recog.listen(source, timeout=10)
    data = " "
    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
        st.write("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)
    return data

def rec_audio_hindi():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak in Hindi...")
        audio = recognizer.listen(source, timeout=10)
    try:
        hindi_text = recognizer.recognize_google(audio, language='hi-IN')
        print(f"Hindi Text: {hindi_text}")
        translator = Translator()
        english_text = translator.translate(hindi_text, dest='en').text
        print(f"English Translation: {english_text}")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as ex:
        print(f"Error connecting to Google Speech Recognition service: {ex}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return english_text

def response(text):# using gtts
    print("Assis:"+text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)

def call(text):
    action_call = "assistant"
    text = text.lower()
    if action_call in text:
        return True
    return False

def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello"]
    response = ["howdy", "whats good", "hello", "hey there"]
    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."
    return ""

from bs4 import BeautifulSoup
import requests
text=requests.get('https://bhuvan.nrsc.gov.in/home/index.php').text #website-home
soup=BeautifulSoup(text,'html.parser')

dictionary={}

jobs=soup.find_all('div', class_='new')
l1=[]
for l in jobs:
    l1.append(l.text)
# print(l1)
key_list = [element.strip().replace('\n', '').replace('\xa0', ' ').replace('\t','').replace('\r','') for element in l1]

# for item in key_list:
#     print(item)

elements = soup.find_all('div', class_='new')
value_list=[]
for k in elements:
        hrefs = [a['href'] for a in k.find_all('a', href=True)]
        for k in hrefs:
                # print(k)
                value_list.append(k)

# print(value_list)
# print(key_list)
my_dict_latest_updates = dict(zip(key_list, value_list))

dictionary.update(my_dict_latest_updates)
dictionary

jobs=soup.find_all('div', class_='col-sm-6 col-lg-2 mbr-col-md-3 col-6')
#print(jobs)
l1=[]
for l in jobs:
    #print(l.text)
    l1.append(l.text)
# print(l1)
key_list = [element.strip().replace('\n', '').replace('\xa0', ' ').replace('\t','').replace('\r','') for element in l1]

# Display the cleaned list
# for item in key_list:
    # print(item)

elements = soup.find_all('div', class_='col-sm-6 col-lg-2 mbr-col-md-3 col-6')
value_list=[]
for k in elements:
        hrefs = [a['href'] for a in k.find_all('a', href=True)]
        for k in hrefs:
                # print(k)
                value_list.append(k)
# print(value_list)
# print(key_list)
my_dict_visual = dict(zip(key_list, value_list))
my_dict_visual

dictionary.update(my_dict_visual)
dictionary

jobs=soup.find_all('div', class_='navbar-nav')
l1 = []
for l in jobs:
    l1.append(l.text)
# print(l1)
key_str=l1[0].split('\n')
key_list = [line for line in key_str if line.strip()]
# print(key_list)
# for item in key_list:
    # print(item, end=' ')
    # print()  # Move to a new line after each item
elements = soup.find_all('div', class_='navbar-nav')
value_list = []

for k in elements:
    hrefs = [a['href'] for a in k.find_all('a', href=True)]
    
    for hre in hrefs:
        if not hre.startswith(('http://', 'https://')):
            if hre.startswith(('#applications_sector')):
                hre = 'https://bhuvan.nrsc.gov.in/home/index.php' + hre
            elif hre.startswith(('collabarators.php')):
                hre = 'https://bhuvan.nrsc.gov.in/home/collabarators.php'
            elif hre.startswith(('#Contact')):
                hre = 'https://bhuvan.nrsc.gov.in/home/index.php#Contact'
            else :
                hre = 'https://bhuvan.nrsc.gov.in/home/newsletter.php'
        
        # print(hre)
        value_list.append(hre)


# print(value_list)
# print(elements_list)
dict_central_appl = dict(zip(key_list, value_list))
dict_central_appl

dictionary.update(dict_central_appl)
dictionary

import speech_recognition as sr
import spacy
from translate import Translator
import webbrowser
import os
import random
import playsound
import pyjokes
#import wolframalpha

nlp = spacy.load("en_core_web_sm")

def get_intent(text):
    doc = nlp(text)
    intent_words = []

    for token in doc:
        if token.dep_ == "ROOT":
            intent_words.append(token.text)

    return " ".join(intent_words)

from fuzzywuzzy import fuzz
import webbrowser

def get_intent(text):
    doc = nlp(text)
    intent_words = [token.text for token in doc if token.dep_ == "ROOT"]
    return " ".join(intent_words)

def fuzzy_intent_match(user_intent, predefined_intent):
    return fuzz.partial_ratio(user_intent, predefined_intent) >= 80

def handle_intent(intent, text):
    speak = ""

    for predefined_intent, url in dictionary.items():
        if fuzzy_intent_match(intent, predefined_intent.lower()):
            webbrowser.open(url)
            speak = f"Opening {predefined_intent}."
            break

    if not speak:
        if intent == "hello":
            speak = say_hello(text)
    return speak

