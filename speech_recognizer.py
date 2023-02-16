from vosk import Model , KaldiRecognizer
import pyaudio


model = Model(r"D:/projects/virtualAssistant/vosk-model-small-lang-en")
recognizer = KaldiRecognizer(model , 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16 , channels = 1 , rate = 16000 , input = True , frames_per_buffer = 8192)
stream.start_stream()

# Speech Recognizer function
def voice_recognizer():
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(text[14:-3])
            break
        else:
            continue
    return text[14:-3]


voice_recognizer()