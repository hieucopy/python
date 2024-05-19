import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb

friday= pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print(' Tro ly : '+ audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time=datetime.datetime.now().strftime('%I:%M:%p')
    speak(Time)
def welcome():
    hour=  datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak('good morning sir')  
    elif hour<20 :
        speak('good afternood sir ')
    else :
        speak('good night sir')
    speak("can i help you ? ")
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio= c.listen(source)
    try:
        
        query = c.recognize_google(audio, language='en')
        print('mr Hieu')
    except sr.UnknownValueError:
        print('speak again or try typing the command')
        query=str(input('the command is : '))
    return query

def new_func():
    return sr.Microphone
if __name__=='__main__':
    
    welcome()
    command()
    # while True:
    #     query=command().lower()
    #     if 'google' in query:
    #         speak('which content you find ?')
    #         search=command().lower()
    #         url= 'https://www.google.com.vn/search?q={search}'
    #         wb.get().open(url)
    #         speak(f'here is your {search} google')