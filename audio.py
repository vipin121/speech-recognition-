import pyaudio
import wave
import speech_recognition as sr
import subprocess


def say(text):
    subprocess.call('say' + text , shell= True)
def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()

def initspeech():
    print("listening....")

    play_audio('./audio/unconvinced.wav')

    with sr.Microphone() as source:
        print("say something......")
        audio = r.listen(source)

    play_audio("./audio/audio_and.wav")

    command = ""

    try:
        command = r.recognize_google(audio)

    except:
        print("couldn't understand u ")

    print("your command:")
    print(command)
    say('you said' + command)

initspeech()
