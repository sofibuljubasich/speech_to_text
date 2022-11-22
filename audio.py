from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence

AUDIO_FILE_MP3 = "mia-nacamulli.mp3" #Link del audio

#Convertir mp3 a wav
audio_mp3 = AudioSegment.from_mp3(AUDIO_FILE_MP3)
audio_mp3.export("transcript.wav", format="wav")
AUDIO_FILE = "transcript.wav"

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio_text = r.listen(source)
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')

