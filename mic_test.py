# http://l34rn-p14y.blogspot.com/2014/11/python-speech-recognition-for-mac-os-x.html
# http://coolestguidesontheplanet.com/setting-up-os-x-mavericks-and-homebrew/
#http://people.csail.mit.edu/hubert/pyaudio/#downloads


# print("should be working")
# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.Microphone() as source:                # use the default microphone as the audio source
#     audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

# print(r.recognize(audio))    # recognize speech using Google Speech Recognition

from pygsr import Pygsr
speech = Pygsr()
speech.record(3) # duration in seconds (3)
phrase, complete_response = speech.speech_to_text('es_ES') # select the language
print phrase