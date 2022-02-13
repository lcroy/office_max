import speech_recognition as sr
import playsound

def speech_to_text_google(cfg):
    # Set American English
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=cfg.sample_rate, chunk_size=cfg.chunk_size, device_index=0) as source:
        # Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise.
        print("Please wait one second for calibrating microphone...")
        r.pause_threshold = 0.8
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source, duration=1)
        print("Ok, microphone is ready...")
        # p = vlc.MediaPlayer(self.hint_sound)
        # p.play()
        playsound.playsound(cfg.hint_sound, True)
        audio = r.listen(source, timeout=None)
        transcript = ""
        try:
            transcript = r.recognize_google(audio, language="en-US")
            print('You: ' + transcript)
        except:
            print('Max: I did not hear anything....')

    return transcript.lower()