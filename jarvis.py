 import pyttsx3
 import speech_recognition as sr
 import datetime
 import wikipedia
 import webbrowser
 import time
 import os
 import pyjokes
 import subprocess as sp
 MASTER = "..."

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am Alexa... How may I help you?")
def takeCommand():
    query = None
    while query is None:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print("Listening...")
            speak("Beep")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language= 'en-in')
        ##
            #query = query.lower()
            #if 'alexa' in query:
                #query = query.replace('alexa', '')
            print(f"user said: {query}\n")
            print(query)
        except Exception:
            print("Say that again please...")
            speak("Say that again please...")
            query = None
        
    if 'Wikipedia' in query:
        query = query.lower()
        speak('Searching in wikipedia....')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'YouTube' in query:
        if 'search' in query:
            speak("{MASTER} what do you want to search")
            query2 = None
            while query2 is None:   
                r2 = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    speak("Beep")
                    audio2 = r2.listen(source, 2)
                    command = r2.recognize_google(audio2)
                    print(command)
                try:
                    print("Recognising...")
                    query2 = r2.recognize_google(audio2, language= 'en-in')
                    print(f"user said: {query2}\n")
                    print(query2)
                    break
                except Exception:
                    print("Say that again please...")
                    speak("Say that again please...")
                    query2 = None
            query2 = query2.replace(" ","+")
            print("eee")
            crome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(crome_path).open(url = "https://www.youtube.com/results?search_query="+query2)
        else:
            crome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(crome_path).open(url = "youtube.com")
        
    elif 'timer' in query:
        speak("{MASTER} for how much time do you want to set?")
        query2 = None
        while query2 is None:   
            r2 = sr.Recognizer()
            with sr.Microphone() as source:
                    print("Listening...")
                    speak("Beep")
                    audio2 = r2.listen(source)
                    print("Done listen")
            try:
                print("Recognising...")
                query2 = r2.recognize_google(audio2, language= 'en-in')
                print(f"user said: {query2}\n")
                print(query2)
                break
            except Exception:
                print("Say that again please...")
                speak("Say that again please...")
                query2 = None
        
        time1 = ""
        for i in query2:
            if i.isdigit():
                time1 = time1 + i
        time2 = int(time1)
        if 'minutes'or 'minute' in query2:
            speak("Ok, your time starts now!")
            time.sleep(60*time2)
            speak("the time is up "+MASTER)
   
        else:
            speak("No timer was set")
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"{MASTER} the time is {strTime}")
        print(strTime)
    elif 'play music' in query:
        music_dir = 'D:\\music'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'open code' in query:
       codepath = "C:\\Users\\91950\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
       os.startfile(codepath)
    
    elif 'Google' in query:
        speak("{MASTER} what do you want to search")
        query2 = None
        while query2 is None:   
            r2 = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                speak("Beep")
                audio2 = r2.listen(source, 2)
                command = r2.recognize_google(audio2)
                print(command)
            try:
                print("Recognising...")
                query2 = r2.recognize_google(audio2, language= 'en-in')
                print(f"user said: {query2}\n")
                print(query2)
                break
            except Exception:
                print("Say that again please...")
                speak("Say that again please...")
                query2 = None
        query2 = query2.replace(" ","+")
        crome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(crome_path).open(url = "https://www.google.com/search?sxsrf=ALeKk03LrBvejjuPt8DAQ
Jem8SQiI9kzog%3A1584946711463&source=hp&ei=F154XsHBGfOf4-EP5rqiiAk&q="+query2+"&oq="+query2+"&gs_l=psy
ab.3..0i131j0j0i131l3j0j0i131j0l2j0i131.1780.2102..2729...2.0..0.181.356.0j2......0....1..gws
wiz.....10..35i362i39j35i39.ewj0sNfGivY&ved=0ahUKEwiBqePNgrDoAhXzzzgGHWadCJEQ4dUDCAY&uact=5") 
    elif 'quit' in query or 'bye' in query:
        speak("Quitting !! Thank u")
        exit()
 def open_camera():
    sp.run('start microsoft.windows.camera:',shell=True)
 def main():
    print("Initializing Alexa")
    speak("Initializing... Alexa...")
    wishMe()
    while True:
        takeCommand()
 main()

