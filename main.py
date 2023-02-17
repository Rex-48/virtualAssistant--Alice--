import pyttsx3

import random 
import os
from wiki_reader import *
from webScrapper import *
# from Search import *
from youtube_downloader import *
from scheduler import *
from automation import *
from set_reminders import *




# text to speech engine function with zira voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


# this function is executed when the command is not recognized

def not_recognized():

    i = rand_num(1,4)
    
    if i == 1 :
        speak("Sorry Cannot Comprehend")

    elif i == 2 :
        speak("can't compute can't comprehend")

    elif i == 3 :
        speak(" coudn't recognize")

    elif i == 4 :
        speak("could u repeat that")




def rand_num():
    return random.randint(0,9)

def rand_num(i,j):
    return random.randint(i,j)

# refrence-links 


command_prompt = " D:/projects/virtualAssistant/References/Command Prompt.lnk "
control_pannel = "D:/projects/virtualAssistant/References/Control Panel.lnk"
e_drive = "D:/projects/virtualAssistant/References/Data (E).lnk"
downloads = "D:/projects/virtualAssistant/References/Downloads.lnk"
file_explorer = "D:/projects/virtualAssistant/References/File Explorer.lnk"
git_bash = "D:/projects/virtualAssistant/References/Git Bash.lnk"
edge_browser = "D:/projects/virtualAssistant/References/Microsoft Edge.lnk"
chrome_Browser = "D:/projects/virtualAssistant/References/Rex - Chrome.lnk"
run_command = "D:/projects/virtualAssistant/References/Run.lnk"
spotify = "D:/projects/virtualAssistant/References/Spotify.lnk"
vs_code = "D:/projects/virtualAssistant/References/Visual Studio Code.lnk"
vlc = "D:/projectsvirtualAssistante/References/VLC media player.lnk"
powerShell = "D:/projects/virtualAssistant/References/Windows PowerShell.lnk"
locate = "D:/projects/virtualAssistant/remider.txt"



speak("core program online")
speak("running error checks")
speak("loading machine learning models and other dependencies")



speak("hello sir good day to u")
speak("i am up , just let me check the error analysis")






from speech_recognizer import *


print("                    ")



while True:

    user_command = str(voice_recognizer())

    user = user_command.lower()

    if "open" in user :

        if "command prompt" in user :
            speak("Affirmative")
            os.startfile(command_prompt)
        
        elif "control pannel" in user :
            speak("Affirmative")
            os.startfile(command_prompt)

        elif "drive e" in user :
            speak("Affirmative")
            os.startfile(e_drive)

        elif "downloads" in user :
            speak("Affirmative")
            os.startfile(downloads)

        elif "file explorer" in user :
            speak("Affirmative")
            os.startfile(file_explorer)

        elif "git bash" in user :
            speak("Affirmative")
            os.startfile(git_bash)

        elif "microsoft edge" in user :
            speak("Affirmative")
            os.startfile(edge_browser)

        elif "google chrome" in user or "chrome" in user or "google" in user :
            speak("Affirmative")
            os.startfile(chrome_Browser)

        elif "run" in user or "win run" in user :
            speak("Affirmative")
            os.startfile(run_command)

        elif "spotify" in user :
            speak("Affirmative")
            os.startfile(spotify)

        elif "vs code" in user or "visual studio code" in user:
            os.startfile(vs_code)

        elif "vlc" in user or "media player" in user :
            os.startfile(vlc)

        elif "power shell" in user or "shell" in user :
            os.startfile(powerShell)




    elif "launch" in user :
        if "command prompt" in user :
            speak("Affirmative")
            os.startfile(command_prompt)
        
        elif "control pannel" in user :
            speak("Affirmative")
            os.startfile(command_prompt)

        elif "drive e" in user :
            speak("Affirmative")
            os.startfile(e_drive)

        elif "downloads" in user :
            speak("Affirmative")
            os.startfile(downloads)

        elif "file explorer" in user :
            speak("Affirmative")
            os.startfile(file_explorer)

        elif "git bash" in user :
            speak("Affirmative")
            os.startfile(git_bash)

        elif "microsoft edge" in user :
            speak("Affirmative")
            os.startfile(edge_browser)

        elif "google chrome" in user or "chrome" in user :
            speak("Affirmative")
            os.startfile(chrome_Browser)

        elif "run" in user or "win run" in user :
            speak("Affirmative")
            os.startfile(run_command)

        elif "spotify" in user :
            speak("Affirmative")
            os.startfile(spotify)

        elif "vs code" in user or "visual studio code" in user:
            speak("Affirmative")
            os.startfile(vs_code)

        elif "vlc" in user or "media player" in user :
            speak("Affirmative")
            os.startfile(vlc)

        elif "power shell" in user or "shell" in user :
            speak("Affirmative")
            os.startfile(powerShell)






    elif "switch" in user :
        led1 = 2
        led2 = 3
        system1 = 4
        system2 = 5

        if "on" in user :
            if "led 1" in user :
                speak("setting pinout voltage to high")
                switch_onn(led1)    

            elif "led 2" in user :
                speak("setting pinout voltage to high")
                switch_onn(led2)

            elif "system 1" in user :
                speak("setting pinout voltage to high")
                switch_onn(system1)

            elif "system 2" in user :
                speak("setting pinout voltage to high")
                switch_onn(system1)

        else:
            if "led 1" in user :
                speak("setting pinout voltage to low")
                switch_off(led1)    

            elif "led 2" in user :
                speak("setting pinout voltage to low")
                switch_off(led2)

            elif "system 1" in user :
                speak("setting pinout voltage to high")
                switch_off(system1)

            elif "system 2" in user :
                speak("setting pinout voltage to high")
                switch_off(system1)



    elif "wikipedia" in user :

        inp = str(user)

        x = int(inp.index("for"))+3
        y = len(inp)
        query = inp[x:y]
        wiki(query)



    elif "anime" in user :
        speak("do u need the directory :")
        response = voice_recognizer()
        if "yes" or "yeah" in response :
            os.startfile("E:\Anime")
        elif "no" in response :
            speak("would u like to me play some movie or a show ")
            res = voice_recognizer()

            if "no" or "nope" or "nah" in res :
                speak("i dont have any other media file beside this")
                speak("i recommend for a server request pull data from the true nas at your home")
                continue
            else :
                speak("playing a random movie from the collection")
                os.startfile("E:\doc\DeadPool 01.mp4")





    elif "reminder" in user :
        speak("Affirmative ..")
        speak("would u like to add or view reminders")
        ext = voice_recognizer()
        if "add" in ext :
            speak("what should i put on the reminder list")
            remind = voice_recognizer()
            
            reminder_write(locate,remind)
        else :
            speak("affirmative")
            speak("here is the reminder list : ")
            reminder_read(locate)

        

    elif "download" and "youtube" and "video" in user :
        speak("okay sir activating the youtube video downlaoder ")
        speak("the video will be downloaded to the current directory")
        speak("now please enter the link for the video down below")
        link = str(input("link here : "))
        downloader(link)

    elif "shedule" in user or "scheduler" in user or "activate scheduler" in user :
        speak("please follow the process now on the screen")
        task_scheduler()

    # elif "spotify play" in user :
    #     pass


    elif "kill" in user:
        if "git-bash" in user :
            speak("terminating")
            os.system("taskkill /f /im mintty.exe")

        elif "google chrome" in user :
            speak("terminating")
            os.system("taskkill /f /im chrome.exe")

        elif "edge_browser" in user :
            speak("terminating")
            os.system("taskkill /f /im msedge.exe")

        elif "vlc" in user :
            speak("terminating")
            os.system("taskkill /f /im vlc.exe")

        elif "visual studio code" in user :
            speak("terminating")
            os.system("taskkill /f /im Code.exe")

        elif "command_prompt" in user :
            speak("terminating")
            os.system("taskkill /f /im cmd.exe")

        elif "spotify" in user :
            speak("terminating")
            os.system("taskkill /f /im Spotify.exe")

        elif "alice" in user :
            speak("terminating")
            exit()

    elif "terminate" in user :
        if "git-bash" in user :
            speak("terminating")
            os.system("taskkill /f /im mintty.exe")

        elif "google chrome" in user :
            speak("terminating")
            os.system("taskkill /f /im chrome.exe")

        elif "edge_browser" in user :
            speak("terminating")
            os.system("taskkill /f /im msedge.exe")

        elif "vlc" in user :
            speak("terminating")
            os.system("taskkill /f /im vlc.exe")

        elif "visual studio code" in user :
            speak("terminating")
            os.system("taskkill /f /im Code.exe")

        elif "command_prompt" in user :
            speak("terminating")
            os.system("taskkill /f /im cmd.exe")

        elif "spotify" in user :
            speak("terminating")
            os.system("taskkill /f /im Spotify.exe")

        elif "self close" in user :
            speak("terminating")
            speak("closing libraries and read and write files")

            exit()

    elif "what is" in user :
        inp = str(user)

        x = int(inp.index("for"))+3
        y = len(inp)
        query = inp[x:y]
        wiki(query)

    elif "scrape" in user or "scrapper" in user or "webbscrapper" in user or "scraping" in user or "web scrapping" in user or "grab links" in user :
        speak("activating web Scrapper")
        scrape_links()

    else :
        not_recognized()