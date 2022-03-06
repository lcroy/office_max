# import azure.cognitiveservices.speech as speechsdk
# import time
#
# def speech_recognize_continuous_from_microphone():
#     audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
#     speech_config = speechsdk.SpeechConfig(subscription="f6bd8f851e48430ea0ea46bb47fad10a", region="northeurope")
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
#
#     done = False
#     result = ''
#     def stop_cb(evt):
#         """callback that stops continuous recognition upon receiving an event `evt`"""
#         nonlocal result
#         result = evt.result.text
#         # Stop continuous speech recognition
#         speech_recognizer.stop_continuous_recognition()
#         nonlocal done
#         done = True
#
#     # Connect callbacks to the events fired by the speech recognizer
#     speech_recognizer.recognized.connect(lambda evt: stop_cb(evt) if evt.result.text != "" else print("No input."))
#
#     # Start continuous speech recognition
#     speech_recognizer.start_continuous_recognition()
#     while not done:
#         time.sleep(.1)
#
#     return result
#
# while True:
#     print("hello")
#     result = speech_recognize_continuous_from_microphone()
#     print("the length of results is: " + str(len(result)))
#
#     print("The result is: " + result)


import azure.cognitiveservices.speech as speechsdk


def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="f6bd8f851e48430ea0ea46bb47fad10a",
                                           region="northeurope")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    while True:
        print("Speak into your microphone.")
        result = speech_recognizer.recognize_once_async().get()
        if len(result.text)>0:
            return result.text
