import speech_recognition as sreg

reg = sreg.Recognizer()
with sreg.Microphone() as input:
    print("You can Speak now :")
    audio = reg.listen(input)
    try:
        content = reg.recognize_google(audio)
        print("What you spoke is: {}".format(content))
    except:
        print("Coundn't understand what you spoke")
