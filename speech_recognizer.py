# from vosk import Model , KaldiRecognizer
# import pyaudio


# model = Model(r"D:/projects/virtualAssistant/vosk-model-en-us-0.22")
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

## THIS HERE ABOVE IS THE CODE FOR VOSK MODEL SPEECH RECOGNITION






def voice_recognizer():
    new = str(input())
    return new
