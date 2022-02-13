import random
import time
import openai

def call_small_talk(max, cfg, text, response_template):
    # Max responses to the small talk
    max_response = random.choice(response_template['small_talk'])
    max.text_to_speech_microsoft(cfg, max_response)
    openai.api_key = cfg.api_key
    while True:
        # waiting for operator's command...
        text = max.speech_to_text_microsoft()
        # quit the small talk service
        if any(key in text.casefold() for key in cfg.trigger_word_quit_small_talk):
            text = random.choice(response_template['quit_small_talk_service'])
            max.text_to_speech_microsoft(cfg, text)
            break

        response = openai.Completion.create(
            engine="davinci",
            prompt= "Human:" + text + "\nAI:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"]
        )
        print(response)
        max_response = response['choices'][0]['text']
        max.text_to_speech_microsoft(cfg, max_response)