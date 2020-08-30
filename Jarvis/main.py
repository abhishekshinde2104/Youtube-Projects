import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import re

#Pre_Processing
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
master = "Abhishek"
query=""
#chrome_path ="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
chrome_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"



#this function will take in text and give out audio
#this function will pronounce the string that is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Aditya is a good boy")

#This function will wish me as per the currnet time
def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning " + master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon " +master)
    else:
        speak("Good evening"+master)

    speak("I am Jarvis . How may i help you ?")


#this function will take command from the microphone
def takeCommand():
    #query = " "
    r = sr.Recognizer()#object
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
        #here its listening the audio
    try:
        #here its recognized
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        #its using googles engine to recoginize audio which it has listened
        #print(f"User said : {qurey}\n")
    except Exception as e:
        #if there is some problem then
        speak("Say that again please")
        query =None
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login('abhishekshinde2104@gmail.com','As@8379007435')
    server.sendmail('gannushinde@gmail.com',to,content)
    server.close()

#Main program starts here
def main():
    speak("Initializing Jarvis...")
    print("Initializing Jarvis...")
    wishMe()
    query=takeCommand()


    #LOGIC FOR EXECUTING TASKS AS PER THE QUERY

    if 'wikipedia' in query.lower():
        speak("Searching wikipedia...")
        query=query.replace("wikipedia","")
        print(query)
        print('\n')
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbroswer.open("youtube.com")
        url="https://www.youtube.com"
        #webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
        #webbrowser.get('chrome').open_new_tab(urL)
        #webbrowser.get(chrome_path).open(url)
        webbrowser.open(url)

    elif 'open google' in query.lower():
        #if r'^search' in query.lower():
        #    word = re.search('^search',query.lower())
        #    print(word)
        #webbroswer.open("youtube.com")
        url="https://google.com"
        #webbrowser.get(chrome_path).open(url)
        webbrowser.open(url)

    elif 'music' in query.lower():
        songs_dir = "E:\\Abhishek\\Songs"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[2]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{master} the time is {strTime}")
        print("The time is : "+strTime)

    elif 'open atom' in query.lower():
        atomPath = "C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\Atom.lnk"
        os.startfile(atomPath)

    elif 'send email' in query.lower():
        try:
            speak("What should i send")
            content = takeCommand()
            to = 'gannushinde@gmail.com'
            sendEmail(to,content)
            #speak("Email has been sent successfully")
        except Exception as e:
            print(e)

    elif 'search' in query.lower():
        try:
            speak("What do want to search : ")
            content = takeCommand()
            url = 'https://www.google.co.in/search?q='
            search_url = url + content
            webbrowser.open(search_url)
        except Exception as e:
            print(e)



main()
