from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, keyphrase='max', kws_threshold=1e-15)
for phrase in speech:
    print(phrase.segments(detailed=True))
