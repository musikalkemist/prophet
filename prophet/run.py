"""This module contains the main entry point for the Prophet application."""

from pathlib import Path

from prophet.audioplayer import AudioPlayer
from prophet.chatgpt import ChatGPT
from prophet.speechrecogniser import SpeechRecogniser
from prophet.speechsynthesiser import GoogleSpeechSynthesiser


def run():
    """This is the main entry point for the Prophet application. It allows
    users to have a conversation with ChatGPT using their voice.
    """

    # Initialise objects
    speech_recogniser = SpeechRecogniser()
    speech_synthesiser = GoogleSpeechSynthesiser()
    audio_player = AudioPlayer()
    chat_gpt = ChatGPT(Path(Path(__file__).parents[1], "chatgptconfig.json"))

    # Conversation loop
    while True:
        print("Listening...")
        text_prompt = speech_recogniser.transcribe()
        print(f"Text input sent to ChatGPT...")
        response = chat_gpt.get_response(text_prompt)
        print(f"Response received from ChatGPT and sent to TTS...")
        audio = speech_synthesiser.synthesise(response)
        print(f"Audio received from TTS and sent to AudioPlayer...")
        audio_player.play(audio)
