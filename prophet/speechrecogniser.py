import speech_recognition as sr


class SpeechRecogniser:
    """This class is used to transcribe audio to text using the
    Google Speech Recognition API called through the SpeechRecognition
    Python library.
    """

    def __init__(self, ambient_adjustement_duration: int = 2) -> None:
        self.recogniser = sr.Recognizer()
        self.mic = sr.Microphone()
        self.text = ""
        self.ambient_adjustement_duration = ambient_adjustement_duration
        self._audio = None

    def transcribe(self) -> str:
        """Transcribe audio to text using the Google Speech Recognition API."""
        self._record_audio()
        try:
            self.text = self.recogniser.recognize_google(self._audio)
            print(f"STT thinks you said: {self.text}")
            return self.text
        except sr.UnknownValueError:
            print("STT could not understand audio")
        except sr.RequestError as e:
            print(f"STT error: {e}")

    def _record_audio(self) -> None:
        with self.mic as source:
            self.recogniser.adjust_for_ambient_noise(
                source, duration=self.ambient_adjustement_duration
            )
            self._audio = self.recogniser.listen(source)


if __name__ == "__main__":
    stt = SpeechRecogniser(2)
    stt.transcribe()
