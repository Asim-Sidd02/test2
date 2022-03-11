from gtts import gTTS
import os
from importlib.resources import path
from unittest import result
from pip import main
import datetime
import speech_recognition as sr
from playsound import playsound
import gtts


def whishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        tts = gtts.gTTS("Good Morining")
        playsound("ge.mp3")
    elif hour>=12 and hour<18:
        tts = gtts.gTTS("Good Afternoon")
        playsound("ge.mp3")  
    else:
        tts = gtts.gTTS("Good evening")
        playsound("ge.mp3")  








def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        tts = gtts.gTTS ("Listening...")
        tts.save("list.mp3")
        playsound("list.mp3")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)


    try:
        print("Recognizing...")
        tts = gtts.gTTS("Recognizing...")
        tts.save("rec.mp3")
        playsound("rec.mp3")

        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)

        print("Say that again...")
        tts = gtts.gTTS("Say that again...")
        tts.save("say.mp3")
        return "None"
    return query


    
    
if __name__ == '__main__':
    
    
   whishMe()
tts = gtts.gTTS("Welcome to KG Reddy College of Engineering And Technology")
tts.save("hell.mp3")
tts = gtts.gTTS("I Am Miss Plexi, How may I help you?")
tts.save("wel.mp3")
playsound("hell.mp3")
playsound("wel.mp3")


while True:
    query = takeCommand().lower()


   
    if 'washroom' in query:
        tts = gtts.gTTS('It is present at each floor, for gents, left side at end, for ladies, right side at end')
        tts.save("was.mp3")
        playsound("was.mp3")


#Ground Flooor
 
    elif 'seminar' in query:
       tts = gTTS("It is at ground floor, move towards right exit of the reception hall, room number G 115")
       tts.save("sem.mp3")
       playsound("sem.mp3")


    elif 'department of student affair' in query:
        tts = gTTS("It is at ground floor, move towards right exit of the reception hall, next to the seminar hall, room number G 114")
        tts.save("dep.mp3")
        playsound("dep.mp3")
   
  