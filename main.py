import os
import time
import speech_recognition as sr
from translate import Translator
from gtts import gTTS

i = 0
NOW_TIME = str(time.time())

translate_from = 'tr-TR'
translate_to = 'en'

while True:
    i = i + 1
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language=translate_from)

            if len(text) > 500:
                print('Please make speeches shorter than 500 words...')
            else:
                print("Perceived: " + text)
                translator = Translator(to_lang=translate_to, from_lang=translate_from)
                translation = translator.translate(text)

                print("Translated: " + translation)
                audio = gTTS(text=translation, lang=translate_to, slow=True)

                if not os.path.isdir(NOW_TIME):
                    os.system("mkdir " + NOW_TIME)
                audio.save(NOW_TIME + "/" + str(i) + ".mp3")
                os.system("afplay " + NOW_TIME + "/" + str(i) + ".mp3")
        except sr.UnknownValueError:
            c = 1