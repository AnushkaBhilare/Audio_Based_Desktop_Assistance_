#from distutils.cmd import Command
#from unittest import result
import pyttsx3 
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
#from PyDictionary import PyDictionary as Diction
import datetime

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("    ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "None"
        
        return query.lower()

query = takecommand()

def OpenApps():
        Speak("Ok Sir! , Wait a second")

        # if 'This PC' in query:
        #     os.startfile("C:\User\This PC")

        if 'excel' in query:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")

        elif 'MS Word' in query:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")

        elif 'PowerPoint' in query:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")

        elif 'Microsoft Edge' in query:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk")

        #elif 'OneDrive' in query:
            #os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneDrive.lnk")

        #elif 'Dell' in query:
        #     os.startfile("C:\Users\Dell")

        #elif 'Google Chrome' in query:
             #os.startfile("C:\Users\Public\Desktop\Google Chrome.lnk")
             #path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
             #webbrowser.get(path).open("google.com")

        # elif 'Firefox' in query:
        #     os.startfile("C:\Users\Public\Desktop\Firefox.lnk")
        
        #elif 'Visual Studio Code' in query:
        #    os.startfile("C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        #elif 'GitHub' in query:
        #    os.startfile("C:\Users\Dell\OneDrive\Desktop\GitHub Desktop.lnk")

        elif 'Whatsapp' in query:
            webbrowser.open('https://www.whatsapp.com/')

        elif 'Facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'Instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'Mail' in query:
            webbrowser.open('https://mail.google.com/')

        elif 'maps' in query:
            webbrowser.open('https://maps.google.com/')

        elif 'Youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        Speak("Your command has been successfully Followed")

def CloseApps():
        Speak("Ok Sir! , Wait a minute")

        if 'This PC' in query:
            os.system("TASKKILL  /f  /in  This PC.exe")

        elif 'excel' in query:
            os.system("TASKKILL  /f  /in  excel.exe")

        elif 'MS Word' in query:
            os.system("TASKKILL  /f  /in  MS Word.exe")

        elif 'PowerPoint' in query:
            os.system("TASKKILL  /f  /in  PowerPoint.exe")

        elif 'Microsoft Edge' in query:
            os.system("TASKKILL  /f  /in  Microsoft Edge.exe")

        elif 'OneDrive' in query:
            os.system("TASKKILL  /f  /in  Onedrive.exe")

        elif 'Dell' in query:
            os.system("TASKKILL  /f  /in  Dell.exe")

        elif 'Google Chrome' in query:
            os.system("TASKKILL  /f  /in  This PC.exe")

        elif 'Firefox' in query:
            os.system("TASKKILL  /f  /in  This PC.exe")
        
        elif 'Visual Studio Code' in query:
            os.system("TASKKILL  /f  /in  Visual Studio Code.exe")

        elif 'GitHub' in query:
            os.system("TASKKILL  /f  /in  GitHub.exe")

        elif 'Whatsapp' in query:
            os.system("TASKKILL  /f  /in  Whatsapp.exe")

        elif 'Facebook' in query:
            os.system("TASKKILL  /f  /in  Facebook.exe")

        elif 'Instagram' in query:
            os.system("TASKKILL  /f  /in  Instagram.exe")

        elif 'Mail' in query:
            os.system("TASKKILL  /f  /in  Mail.exe")

        elif 'maps' in query:
            os.system("TASKKILL  /f  /in  maps.exe")

        elif 'Youtube' in query:
            os.system("TASKKILL  /f  /in  Youtube.exe")

        Speak("Your command has been successfully Followed")

def Music():

        Speak("Tell me the name of the song!")
        musicName = takecommand()
    
        if 'Jhoom' in musicName:
            os.startfile('C:\\Users\\Dell\\Downloads\\Jhoom.mpeg')

        elif 'Rang lageya' in musicName:
            os.startfile('C:\\Users\\Dell\\Downloads\\Rang lageya.mpeg')
        
        elif 'Jaan ban gaye' in musicName:
            os.startfile('C:\\Users\\Dell\\Downloads\\Jaan ban gaye.mpeg')

        elif 'Sari duniya se' in musicName:
            os.startfile('C:\\Users\\Dell\\Downloads\\Sari duniya se.mpeg')
        
        else:
            pywhatkit.playonyt(musicName)

        Speak("Your song has been started! , Enjoy Sir!")

def Whatsapp():
        Speak("Tell me the name of the person!")
        name = takecommand()

        if 'Abhishek' in name:
            Speak("Tell me the message!")
            msg = takecommand()
            Speak("Tell me the time Sir!")
            Speak("Time in hours!")
            hour = int(takecommand())
            Speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918390094799",msg,hour,min,20)
            Speak("Ok Sir,Sending Whatsapp message !")
        
        
        elif 'Vrutti' in name:
            Speak("Tell me the message!")
            msg = takecommand()
            Speak("Tell me the time Sir!")
            Speak("Time in hours!")
            hour = int(takecommand())
            Speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+917045404888",msg,hour,min,20)
            Speak("Ok Sir,Sending Whatsapp message !")

        elif 'Shreya' in name:
            Speak("Tell me the message!")
            msg = takecommand()
            Speak("Tell me the time Sir!")
            Speak("Time in hours!")
            hour = int(takecommand())
            Speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+917718982002",msg,hour,min,20)
            Speak("Ok Sir,Sending Whatsapp message !")

        elif 'Vishal' in name:
            Speak("Tell me the message!")
            msg = takecommand()
            Speak("Tell me the time Sir!")
            Speak("Time in hours!")
            hour = int(takecommand())
            Speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918591210614",msg,hour,min,20)
            Speak("Ok Sir,Sending Whatsapp message !")

        else:
            Speak("Tell me the phone number")
            phone = int(takecommand())
            ph = '+91' + phone
            Speak("Tell me the message!")
            msg = takecommand()
            Speak("Tell me the time Sir!")
            Speak("Time in hours!")
            hour = int(takecommand())
            Speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Ok Sir,Sending Whatsapp message !")

""" def Dict():
        Speak("Activated Dictionary!")
        Speak("Tell me the Problem")
        prob1 = takecommand()
        dict=Diction()
        if 'meaning' in prob1:
            prob1 = prob1.replace("what is the", " ")
            prob1 = prob1.replace("jarvis"," ")
            prob1 = prob1.replace("of")
            prob1 = prob1.replace("meaning of", " ")
            result = dict.meaning(prob1)
            Speak(f"The meaning for {prob1} is {result}")

        elif 'synonym' in prob1:
            prob1 = prob1.replace("what is the", " ")
            prob1 = prob1.replace("jarvis"," ")
            prob1 = prob1.replace("of")
            prob1 = prob1.replace("synonym of", " ")
            result = dict.synonym(prob1)
            Speak(f"The synonym for {prob1} is {result}")

        elif 'antonym' in prob1:
            prob1 = prob1.replace("what is the", " ")
            prob1 = prob1.replace("jarvis"," ")
            prob1 = prob1.replace("of")
            prob1 = prob1.replace("antonym of", " ")
            result = dict.antonym(prob1)
            Speak(f"The antonym for {prob1} is {result}")

        Speak("Exited Dictionary!!") """

def YoutubeAuto():
        Speak("What is your command ??")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'file mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

def ChromeAuto():
    Speak("Chrome Automation Started !")

    command = takecommand()

    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')

    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')

    elif 'history' in command:
        keyboard.press_and_release('crtl + h')

def screenshot():
    Speak("Ok, What Should I name that file?")
    path = takecommand()
    path1name = path + ".png"
    path1 = "C:\\Users\\Dell\\OneDrive\\Pictures\\Screenshots" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("C:\\Users\\Dell\\OneDrive\\Pictures\\Screenshots")
    Speak("Here is your screenshort")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        Speak("Good Morning")
    elif hour >= 12 and hour < 17 :
        Speak("Good Afternoon")
    else:
        Speak("Good Evening")
    Speak("I am Jarvis mam, how may i help you?")

def TaskExe():
    
    wishMe()
    
    while True:
        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I'm Jarvis.")
            Speak("You'r Personal AI Assistant!")
            Speak("How may I help you?")

        elif 'Namaste' in query:
            Speak("Namaste")
            Speak("Mein apka AI Assiatant!")
            Speak("Mein apki kis prakar sahaayata kar sakta hoon")
        
        elif 'How are you' in query:
            Speak("I'm fine sir!")
            Speak("What about you?")

        elif 'You need a break' in query:
            Speak("Ok Sir , you can call me anytime !")
            break

        elif 'kya haal hai' in query:
            Speak("Mein Badiya hoon , app btao !")

        elif 'bye' in query:
            Speak("Ok Sir , Bye!")
            break
        
        elif 'Mein accha hoon' in query:
            Speak("Mein bhi !")

        elif 'Youtube Search' in query:
            Speak ("Ok Sir , This is what found for your search !")
            query = query.replace("jarvis" , "")
            query = query.replace("youtube search" , "")
            web = 'https://www.youtube.com/results?search_query=' + query
            Speak("Done Sir !")
        
        elif 'Google Search' in query:

            Speak("This is what I found for your search sir !")
            query = query.replace("jarvis" , "")
            query = query.replace("Google Search" , "")
            pywhatkit.search(query)
            Speak("Done Sir !")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" "," ")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched !")

        elif 'launch' in query:
            Speak("Tell me the name of the website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")
        
        elif 'music' in query:
            Music()
        
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to Wikipedia : (wiki)")

        elif 'whatsapp meaasage' in query:
            Whatsapp()  

        elif 'screenshot' in query:
            screenshot()

        elif 'open This PC' in query:
            OpenApps()

        elif 'open excel' in query:
            OpenApps()

        elif 'open MS Word' in query:
            OpenApps()

        elif 'open PowerPoint' in query:
            OpenApps()

        elif 'open Microsoft Edge' in query:
            OpenApps()

        elif 'open OneDrive' in query:
            OpenApps()

        elif 'open Dell' in query:
            OpenApps()

        elif 'open Google Chrome' in query:
            OpenApps()

        elif 'open Firefox' in query:
            OpenApps()
        
        elif 'open Visual Studio Code' in query:
            OpenApps()

        elif 'open GitHub' in query:
            OpenApps()

        elif 'open Whatsapp' in query:
            OpenApps()

        elif 'open Facebook' in query:
            OpenApps()

        elif 'open Instagram' in query:
            OpenApps()

        elif 'open Mail' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open Youtube' in query:
            OpenApps()

        elif 'close This PC' in query:
            CloseApps()

        elif 'close excel' in query:
            CloseApps()

        elif 'close MS Word' in query:
            CloseApps()

        elif 'close PowerPoint' in query:
            CloseApps()

        elif 'close Microsoft Edge' in query:
            CloseApps()

        elif 'close OneDrive' in query:
            CloseApps()

        elif 'close Dell' in query:
            CloseApps()

        elif 'close Google Chrome' in query:
            CloseApps()

        elif 'close Firefox' in query:
            CloseApps()
        
        elif 'close Visual Studio Code' in query:
            CloseApps()

        elif 'close GitHub' in query:
            CloseApps()

        elif 'close Whatsapp' in query:
            CloseApps()

        elif 'close Facebook' in query:
            CloseApps()

        elif 'close Instagram' in query:
            CloseApps()

        elif 'close Mail' in query:
            CloseApps()

        elif 'close maps' in query:
            CloseApps()

        elif 'close Youtube' in query:
            CloseApps()
        
        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'file mode' in query:
            keyboard.press('t')

        elif 'pause' in query:
            keyboard.press('k')

        elif 'youtube tool' in query:
            YoutubeAuto() 

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('crtl + h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my words' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You said : {jj}")

        elif 'my location' in query:
            Speak("Ok Sir, Wait a minute!")
            webbrowser.open('')   

        """ elif 'dictionary' in query:
            Dict()
             """
