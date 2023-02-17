# from vosk import Model , KaldiRecognizer
# import pyaudio


# model = Model(r"D:/projects/virtualAssistant/vosk-model-small-lang-en")
# recognizer = KaldiRecognizer(model , 16000)
# mic = pyaudio.PyAudio()
# stream = mic.open(format=pyaudio.paInt16 , channels = 1 , rate = 16000 , input = True , frames_per_buffer = 8192)
# stream.start_stream()

# # Speech Recognizer function
# def voice_recognizer():
#         data = stream.read(4096)
#         if recognizer.AcceptWaveform(data):
#             text = recognizer.Result()
#             print(text[14:-3])
#             return text[14:-3]
#         else:
#             voice_recognizer()

# ## THIS HERE ABOVE IS THE CODE FOR VOSK MODEL SPEECH RECOGNITION


def voice_recognizer():
    new = str(input("user : "))
    return new

# import speech_recognition as sr

# def voice_recognizer():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=0.2)
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         print("by product")
#         query = r.recognize_google(audio, language='en-us')

#         print("user said : "+query)

#     except Exception as e:    
#         print("Say that again please...")  
#         return "None"
#     return query


