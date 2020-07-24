import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 122)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am viz, how may i help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def NewsFromBBC(): 
	
	# BBC news api 
	main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=17afa8fb6d7c490c93ba2f727e8f3e62"

	# fetching data in json format 
	open_bbc_page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = open_bbc_page["articles"] 

	# empty list which will 
	# contain all trending news 
	result = [] 
	
	for ar in article: 
		result.append(ar["title"]) 
		
	for i in range(len(result)): 
		
		# printing all trending news 
		print(i + 1, result[i]) 

	#to read the news out loud for us 
	from win32com.client import Dispatch 
	speak = Dispatch("SAPI.Spvoice") 
	speak.Speak(result)				 

       

if __name__ == "__main__":
    wishMe()
    while True:
        text = takeCommand()
        


        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
           music_dir = 'your_location'
           songs = os.listdir(music_dir)
           print(songs)    
           os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'news' in query:
            NewsFromBBC()

        elif 'bye bye' in query:
            speak("hope I was helpful")
            exit()
 