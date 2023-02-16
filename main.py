import pyttsx3
from speech_recognizer import *
import random 
import os
from wiki_reader import *
from webScrapper import *
from Search import *
from youtube_downloader import *
from scheduler import *
from automation import *
from set_reminders import *




# text to speech engine function with zira voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(text):
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



while True:
    user_command = voice_recognizer()

    user = user_command.lower()

    if "open" in user :

        if "command prompt" in user :
            os.startfile(command_prompt)
        
        elif "control pannel" in user :
            os.startfile(command_prompt)

        elif "drive e" in user :
            os.startfile(e_drive)

        elif "downloads" in user :
            os.startfile(downloads)

        elif "file explorer" in user :
            os.startfile(file_explorer)

        elif "git bash" in user :
            os.startfile(git_bash)

        elif "microsoft edge" in user :
            os.startfile(edge_browser)

        elif "google chrome" in user or "chrome" in user :
            os.startfile(chrome_Browser)

        elif "run" in user or "win run" in user :
            os.startfile(run_command)

        elif "spotify" in user :
            os.startfile(spotify)

        elif "vs code" in user or "visual studio code" in user:
            os.startfile(vs_code)

        elif "vlc" in user or "media player" in user :
            os.startfile(vlc)

        elif "power shell" in user or "shell" in user :
            os.startfile(powerShell)







    elif "automation" in user :
        pass





    elif "fire" in user :
        pass








    elif "launch" in user :
        if "command prompt" in user :
            os.startfile(command_prompt)
        
        elif "control pannel" in user :
            os.startfile(command_prompt)

        elif "drive e" in user :
            os.startfile(e_drive)

        elif "downloads" in user :
            os.startfile(downloads)

        elif "file explorer" in user :
            os.startfile(file_explorer)

        elif "git bash" in user :
            os.startfile(git_bash)

        elif "microsoft edge" in user :
            os.startfile(edge_browser)

        elif "google chrome" in user or "chrome" in user :
            os.startfile(chrome_Browser)

        elif "run" in user or "win run" in user :
            os.startfile(run_command)

        elif "spotify" in user :
            os.startfile(spotify)

        elif "vs code" in user or "visual studio code" in user:
            os.startfile(vs_code)

        elif "vlc" in user or "media player" in user :
            os.startfile(vlc)

        elif "power shell" in user or "shell" in user :
            os.startfile(powerShell)

        else :
            not_recognized()





    elif "switch" in user :
        led1 = 2
        led2 = 3
        system1 = 4
        system2 = 5

        if "led1" in user :
            switch1(led1)

        elif "led2" in user :
            switch1(led2)

        elif "system 1" in user :
            switch1(system1)

        elif "system 2" in user :
            switch1(system2)        


    elif "wikipedia" in user :

        inp = str(user)

        x = int(inp.index("for")+3)
        y = len(inp)
        query = inp[x:y]
        wiki(query)


    elif "search" in user :
        x = int(inp.index("for")+3)
        y = len(inp)
        que = inp[x:y]
        webSearch(que)



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

    elif "shedule"or "scheduler" or "activate scheduler" in user :
        speak("please follow the process now on the screen")
        task_scheduler()

    # elif "spotify play" in user :
    #     pass

    elif "kill" in user:
        if "git-bash" in user :
            os.system("taskkill /f /im mintty.exe")

        elif "Google Chrome" in user :
                os.system("taskkill /f /im chrome.exe")

        elif "edge_browser" in user :
                os.system("taskkill /f /im msedge.exe")

        elif "vlc" in user :
                os.system("taskkill /f /im vlc.exe")

        elif "Visual Studio Code" in user :
                os.system("taskkill /f /im Code.exe")

        elif "Command_Prompt" in user :
                os.system("taskkill /f /im cmd.exe")

        elif "Spotify" in user :
                os.system("taskkill /f /im Spotify.exe")

        elif "self close" in user :
                exit()

    elif "terminate" in user :
        if "git-bash" in user :
            os.system("taskkill /f /im mintty.exe")

        elif "Google Chrome" in user :
                os.system("taskkill /f /im chrome.exe")

        elif "edge_browser" in user :
                os.system("taskkill /f /im msedge.exe")

        elif "vlc" in user :
                os.system("taskkill /f /im vlc.exe")

        elif "Visual Studio Code" in user :
                os.system("taskkill /f /im Code.exe")

        elif "Command_Prompt" in user :
                os.system("taskkill /f /im cmd.exe")

        elif "Spotify" in user :
                os.system("taskkill /f /im Spotify.exe")

        elif "self close" in user :
                exit()

    elif "what is" in user :
        inp = str(user)

        x = int(inp.index("for")+3)
        y = len(inp)
        query = inp[x:y]
        wiki(query)

    elif "scrape" or "scrapper" or "webbscrapper" or "scraping" or "web scrapping"  or "grab links" in user :
        speak("activating web Scrapper")
        scrape_links()






