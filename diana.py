import speech_recognition as sr
import playsound
from gtts import gTTS, tts
import random
import webbrowser
import pyttsx3
import os

class Virtual_assist():
    def __init__(self, assist_name, person):
        self.person = person
        self.assist_name = assist_name

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()

        self.voice_data = ''

    def engine_speak(self, text):
          
        #fala da assistente virtual

        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def record_audio(self, ask=""):


        with sr.Microphone() as source:
            if ask:
                print('recording...')
                self.engine_speak(ask)

            audio = self.r.listen(source, 5, 5) # pega dados de audio
            print('looking at the data base')
            try:
                self.voice_data = self.r.recognize_google(audio) # converte audio para texto

            except sr.UnknownValueError:
                self.engine_speak('Sorry Boss, I did not get what you said. Can you please repeat?')

            except sr.RequestError:
                self.engine_speak('Sorry Boss, my server is down') # recognizer is not connected   

            print(">>",self.voice_data.lower()) # imprime o que for dito
            self.voice_data = self.voice_data.lower()
            print("-------------------------------------------------------------------------------- ")

            return self.voice_data.lower()

    def engine_speak(self, audio_string):
        audio_string = str(audio_string)
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 20000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(self.assist_name + ':', audio_string)
        os.remove(audio_file)


    def there_exist(self, terms):
        
        #função para identificar se o termo existe

        for term in terms:
            if term in self.voice_data:
                return True


    def respond(self, voice_data):
        if self.there_exist(['hey', 'hi', 'hello', 'oi', 'holla']):
            greetigns = [f'Hi {self.person}, what are we doing today?',
                        'Hi Boss, how can I help you?',
                        'Hi Boss, what do you need?']

            greet = greetigns[random.randint(0,len(greetigns)-1)]
            self.engine_speak(greet)

        #google
        if self.there_exist(['search for']) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url =  "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("here is what I found for " + search_term + 'on google')

        #google 
        if self.there_exist(["search youtube for"]):
            search_term  = voice_data.split("for")[-1]
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak("Here is what i found for" + search_term + 'on youtube')


        #OLD PC FUNCTIONS :( TO UPDATE :) start msi Mystic Light
        if self.there_exist(['open mystic light']):
            self.engine_speak("Opening msi Mystic Light")
            os.startfile("C:\Program Files (x86)\MSI\Mystic Light\Mystic Light.exe")

        if self.there_exist(['close']):
            self.engine_speak("Closing msi Mystic Light")
            os.system("taskkill /F /IM Mystic Light.exe /T")

        if self.there_exist(['microsoft word']):
            self.engine_speak(["Opening Microsoft Word"])
            os.startfile("C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")


assistent = Virtual_assist('Diana', 'Pierro')

while True:

    voice_data = assistent.record_audio('listening...')
    assistent.respond(voice_data)

    if assistent.there_exist(['bye', 'goodbye', 'seeyou', 'see you later', 'see you']):
        assistent.engine_speak("Have a nice day sir, good bye!")
        break