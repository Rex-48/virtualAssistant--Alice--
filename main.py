import pyttsx3
from speech_recognizer import *
import random 
import os
from wiki_reader import *
from webScrapper import *

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
        pass

    elif "wikipedia" in user :

        inp = str(user)

        x = int(inp.index("for")+3)
        y = len(inp)
        query = inp[x:y]
        wiki(query)


    elif "search" in user :
        pass

    elif "anime" in user :
        pass

    elif "set reminder" in user :
        pass

    elif "download" and "youtube" and "video" in user :
        pass

    elif "shedule" in user :
        pass

    elif "spotify play" in user :
        pass

    elif "kill" in user:
        if "git-bash" in user :
        os.system("taskkill /f /im mintty.exe")

        elif "Google Chrome" in user :
                os.system("taskkill /f /im chrome.exe")

        elif "edge_browser" in user 
                os.system("taskkill /f /im msedge.exe")

        elif "vlc" in user
                os.system("taskkill /f /im vlc.exe")

        elif "Visual Studio Code" in user
                os.system("taskkill /f /im Code.exe")

        elif "Command_Prompt" in user
                os.system("taskkill /f /im cmd.exe")

        elif "Spotify" in user
                os.system("taskkill /f /im Spotify.exe")

        elif "self close" in user
                exit()

    elif "terminate" in user :
        pass

    elif "what is" in user :
        inp = str(user)

        x = int(inp.index("for")+3)
        y = len(inp)
        query = inp[x:y]
        wiki(query)

    elif "scrape" or "scrapper" or "webbscrapper" or "scraping" or "web scrapping"  or "grab links" in user :
        speak("activating web Scrapper")
        scrape_links()






