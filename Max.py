import speech_recognition as sr
import random
import boto3
import playsound
import pyttsx3
import azure.cognitiveservices.speech as speechsdk
import time
import requests
import pygame
import subprocess
import json
import datetime
from pocketsphinx import LiveSpeech
from test import *

from small_talk_service.call_small_talk_service import call_small_talk
from messenger_service.call_message_service import call_message
from dboperation import *

# from pygame import *
# import vlc
from configure import Config

class Max:

    def __init__(self, cfg):
        self.sample_rate = cfg.sample_rate
        self.chunk_size = cfg.chunk_size
        self.hint_sound = cfg.hint_sound
        self.voice = cfg.voice_id
        self.converter = pyttsx3.init()
        self.converter.setProperty('rate', 150)
        self.converter.setProperty('volume', 0.7)
        self.host = cfg.max_server_host
        self.headers = {'Content-Type': 'application/json', 'Accept-Language': 'en_US'}

    # Google service to recognize the speech
    def speech_to_text_google(self):
        """performs keyword-triggered speech recognition with input microphone"""
        speech_config = speechsdk.SpeechConfig(subscription="946996bf23eb4cd583aecb0a2c3ad040", region="northeurope")

        # Creates an instance of a keyword recognition model. Update this to
        # point to the location of your keyword recognition model.
        model = speechsdk.KeywordRecognitionModel("973bb8bd-9de7-4921-9b73-ec8644513730.table")

        # The phrase your keyword recognition model triggers on.
        keyword = "hey max"

        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        done = False
        result = ''

        def stop_cb(evt):
            """callback that signals to stop continuous recognition upon receiving an event `evt`"""
            print('CLOSING on {}'.format(evt))
            nonlocal done
            done = True

        def recognizing_cb(evt):
            """callback for recognizing event"""
            if evt.result.reason == speechsdk.ResultReason.RecognizingKeyword:
                print('RECOGNIZING KEYWORD: {}'.format(evt))
            elif evt.result.reason == speechsdk.ResultReason.RecognizingSpeech:
                print('RECOGNIZING: {}'.format(evt))

        def recognized_cb(evt):
            """callback for recognized event"""
            nonlocal result
            result = evt.result.text
            print("User said:" + result)
            if evt.result.reason == speechsdk.ResultReason.RecognizedKeyword:
                print('RECOGNIZED KEYWORD: {}'.format(evt))
            elif evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print('RECOGNIZED: {}'.format(evt))
            elif evt.result.reason == speechsdk.ResultReason.NoMatch:
                print('NOMATCH: {}'.format(evt))

        # Connect callbacks to the events fired by the speech recognizer
        speech_recognizer.recognizing.connect(recognizing_cb)
        speech_recognizer.recognized.connect(recognized_cb)
        speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
        speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
        # stop continuous recognition on either session stopped or canceled events
        speech_recognizer.session_stopped.connect(stop_cb)
        speech_recognizer.canceled.connect(stop_cb)

        # Start keyword recognition
        speech_recognizer.start_keyword_recognition(model)
        print('Max: now you can call Max.'.format(keyword))
        while not done:
            time.sleep(.5)

        speech_recognizer.stop_keyword_recognition()
        return result.lower()

        # speech = LiveSpeech(lm=False, keyphrase='max', kws_threshold=1e-20)
        # print("Max: You can call the keywords now...")
        # for phrase in speech:
        #     list = phrase.segments(detailed=True)
        #     if len(list) > 0:
        #         try:
        #             if ((list[0][0] == 'max') or (list[0][0] == 'Max')):
        #                 print(list[0][0])
        #                 return 'Max'
        #         except:
        #             continue
        # # Set American English
        # r = sr.Recognizer()
        # with sr.Microphone(sample_rate=self.sample_rate, chunk_size=self.chunk_size, device_index=0) as source:
        #     # Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise.
        #     print("Please wait one second for calibrating microphone...")
        #     r.pause_threshold = 0.8
        #     r.dynamic_energy_threshold = True
        #     r.adjust_for_ambient_noise(source, duration=1)
        #     print("Ok, microphone is ready...")
        #     # p = vlc.MediaPlayer(self.hint_sound)
        #     # p.play()
        #     playsound.playsound(self.hint_sound, True)
        #     audio = r.listen(source, timeout = None)
        #     transcript = ""
        #     try:
        #         transcript = r.recognize_google(audio, language="en-US")
        #         print('You: ' + transcript)
        #     except:
        #         print('Max: I did not hear anything....')
        #
        # return transcript.lower()

    # Microsoft service to recognize speech
    def speech_to_text_microsoft(self):
        speech_config = speechsdk.SpeechConfig(subscription="f6bd8f851e48430ea0ea46bb47fad10a",
                                               region="northeurope")
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

        while True:
            print("Speak into your microphone.")
            result = speech_recognizer.recognize_once_async().get()
            if len(result.text) > 0:
                return result.text
        # audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        # speech_config = speechsdk.SpeechConfig(subscription="f6bd8f851e48430ea0ea46bb47fad10a", region="northeurope")
        # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        #
        # done = False
        # result = ''
        #
        # def stop_cb(evt):
        #     """callback that stops continuous recognition upon receiving an event `evt`"""
        #     nonlocal result
        #     result = evt.result.text
        #     # Stop continuous speech recognition
        #     speech_recognizer.stop_continuous_recognition()
        #     nonlocal done
        #     done = True
        #     print("User: " + result)
        #
        # # Connect callbacks to the events fired by the speech recognizer
        # speech_recognizer.recognized.connect(lambda evt: stop_cb(evt) if evt.result.text != "" else print("Max: I did not hear anything..."))
        #
        # # Start continuous speech recognition
        # speech_recognizer.start_continuous_recognition()
        # while not done:
        #     time.sleep(.1)
        #
        # return result.lower()

    # Text to Speech - generate audio file
    def generate_botx_res_mp3(self, cfg, text):
        poly = boto3.client('polly')
        response = poly.synthesize_speech(OutputFormat='mp3', Text=text, VoiceId=self.voice)
        body = response['AudioStream'].read()
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        file_name = cfg.voice_path + now + r"speakervoice.mp3"
        try:
            f = open(file_name, "wb+")
            f.write(body)
        except IOError:
            print("Sorry, I can not create the audio file")
        else:
            f.close()

        return file_name

    # Text to Speech - Amazon Polly service
    def text_to_speech(self, cfg, text):
        print('Max: ' + text)
        # generate the response mp3
        mp3_file_path = self.generate_botx_res_mp3(cfg, text)
        playsound.playsound(mp3_file_path)
        # p = vlc.MediaPlayer(mp3_file_path)
        # p.play()

    def text_to_speech_local(self, text):
        print('BotX: ' + text)
        self.converter.say(text)
        self.converter.runAndWait()

    def text_to_speech_microsoft(self, cfg, text):
        # Creates an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").
        speech_key, service_region = "f6bd8f851e48430ea0ea46bb47fad10a", "northeurope"
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"

        # Creates a speech synthesizer using the default speaker as audio output.
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        print("Max: " + text)
        # p_typing_audio = subprocess.Popen(["python", cfg.typing_audio_script])
        result = speech_synthesizer.speak_text(text)
        # p_typing_audio.terminate()

    def get_response(self, text, requested_service, client_slot_result):
        parameters = {'message':text, 'requested_service': requested_service, 'client_slot_result':client_slot_result}
        result = requests.get(self.host + 'get_service/', params=parameters, headers=self.headers)

        return result.json()

    def get_file(self):
        result = requests.get(self.host + 'download', headers=self.headers)

        return result.json()

    def greeting_based_on_time(self):
        # Check the time
        greeting = ""
        hour = datetime.datetime.now().hour
        if hour < 8:
            greeting = random.choice(["Hi Morning, you are very early today ","Good morning, it is quite early "])
        if hour < 12:
            greeting = random.choice(["Hi morning ","Good morning "])
        elif hour < 16:
            greeting = random.choice(["Hi good afternoon "])
        else:
            greeting = "Good evening "

        return greeting

    def call_max(self, cfg):
        # new a configure file
        cfg = Config()
        #read response template from json file
        with open(cfg.response_template) as json_file:
            response_template = json.load(json_file)
        while True:
            # set defatult status is write
            status_results = status(cfg.dataset_path_db, "update", "write", "no_one_care")
            # 1. check the trigger word
            print("You may talk to Max now...")
            # update to the response to the db
            reply_result = res_max(cfg.dataset_path_db, 'write', "Call Max, if you need a message service :)")
            text = self.speech_to_text_google().casefold()
            # if system detects the trigger word - Max
            if any(key in text.casefold() for key in cfg.trigger_word_max):
                text = self.greeting_based_on_time()
                # update to the response to the db
                reply_result = res_max(cfg.dataset_path_db, 'write', text)
                self.text_to_speech_microsoft(cfg, text)
                call_message(self, cfg, text, response_template)
                # text = random.choice(response_template['init_speak'])
                # self.text_to_speech_microsoft(cfg, text)
                # while True:
                #     # 2. wait for human command
                #     text = self.speech_to_text_microsoft().casefold()
                #     # BotX does heard something not some random noise
                #     if len(text) > 0:
                #
                #         # call small talk service
                #         if any(key in text.casefold() for key in cfg.trigger_word_small_talk):
                #             call_small_talk(self, cfg, text, response_template)
                #             break
                #
                #         # call max to introduce his basic functions
                #         if any(key in text.casefold() for key in cfg.trigger_word_introduce_capability):
                #             text = random.choice(response_template['introduce_service'])
                #             self.text_to_speech_microsoft(cfg, text)
                #             break
                #
                #         # call max to message service
                #         if any(key in text.casefold() for key in cfg.trigger_word_message_service):
                #             call_message(self, cfg, text, response_template)
                #             # text = random.choice(response_template['message_service'])
                #             break
                #
                #         text = random.choice(response_template['max_do_not_understand'])
                #         self.text_to_speech_microsoft(cfg, text)
                #         break