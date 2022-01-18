import speech_recognition as sr #we need this package inorder to recognize the user voice.
import pyttsx3 #this package is used to speak out the ouput voice of our assistant.
import pywhatkit #we use this package to instantiate the request from the user.
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() # this listener will recognize your voice with the help of Recognizer() method.
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[2].id) #this statement is used to set the voices for our assistant.


def talk(text):
        engine.say(text)            #this function will allow out AI to speak the user request.
        engine.runAndWait()

def take_command():                 #this function allows the AI to take command from the user.
    try:
        with sr.Microphone() as source: # with help of Microphone you can speak to your Assistant.
            print('listening...')
            voice = listener.listen(source) #using the listen() method we will listen to the voice getting from the  user.
            command = listener.recognize_google(voice) #the request from the user is stored in this variable.
            command = command.lower()

            if 'paradox' in command:
                command = command.replace('paradox','') #this prints the request of the user on the console.

                print(command)
    except:
        pass
    return command

def run_paradox():          #it will run our AI.
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk(f'playing{song}')
        pywhatkit.playonyt(song)        #using this package statement we make our song play from the youtube.
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')     #this will show the time.
        talk('the time is '+time)
    elif 'search' in command:
        value=command.replace('search','')
        info=wikipedia.summary(value,1)             #this package statement is usded to give the required info from the wikipedia.
        print(info)
        talk(info)
    elif 'my name' in command:
        talk('your name is Nagendra Marisetti')
    elif 'your name' in command:
        talk('my name is Paradox. I am the personal AI assistant for Nagendra Marisetti')
    elif 'joke'  in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry! Please say the command once again')


while True:
    run_paradox()