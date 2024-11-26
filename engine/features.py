from playsound import playsound
import eel

#playing Start sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\Siri_Sound_Effect_HD.mp3"
    playsound(music_dir)