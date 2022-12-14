import os

import google.cloud.texttospeech as tts


class GoogleSpeechSynthesiser:
    """GoogleSpeechSynthesiser is a wrapper around the Google Cloud
    Text-To-Speech API, which is responsible to synthesise speech from text.
    """

    def __init__(
        self, language_code: str = "en-GB", voice_name: str = "en-GB-Neural2-A"
    ) -> None:
        self._client = tts.TextToSpeechClient()
        self._voice = tts.VoiceSelectionParams(
            language_code=language_code, name=voice_name
        )
        self._audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)

    def synthesise(self, text: str):
        """Synthesise text making a call to the Google Cloud
        Text-To-Speech API.

        Args:
            text: The text to synthesise.
        Returns:
            Binary object containing synthesised speech
        """
        synthesis_input = tts.SynthesisInput(text=text)
        response = self._client.synthesize_speech(
            input=synthesis_input, voice=self._voice, audio_config=self._audio_config
        )
        return response.audio_content
