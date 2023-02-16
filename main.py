import pyttsx3
from speech_recognizer import *
import os





# text to speech engine function with zira voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()





# refrence-links 


command_prompt = " D:/projects/Alice/References/Command Prompt.lnk "
control_pannel = "D:/projects/Alice/References/Control Panel.lnk"
e_drive = "D:/projects/Alice/References/Data (E).lnk"
downloads = "D:/projects/Alice/References/Downloads.lnk"
file_explorer = "D:/projects/Alice/References/File Explorer.lnk"
git_bash = "D:/projects/Alice/References/Git Bash.lnk"
edge_browser = "D:/projects/Alice/References/Microsoft Edge.lnk"
chrome_Broser = "D:/projects/Alice/References/Rex - Chrome.lnk"
run_command = "D:/projects/Alice/References/Run.lnk"
spotify = "D:/projects/Alice/References/Spotify.lnk"
vs_code = "D:/projects/Alice/References/Visual Studio Code.lnk"
vlc = "D:/projects/Alice/References/VLC media player.lnk"
powerShell = "D:/projects/Alice/References/Windows PowerShell.lnk"


'''

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
            os.startfile(chrome_Broser)

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

 #   elif "play music" in user :
        






'''
















