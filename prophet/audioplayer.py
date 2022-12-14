from pydub import AudioSegment
from pydub.playback import play

from prophet.utils import save_file, delete_file


class AudioPlayer:
    """AudioPlayer is responsible to play audio files."""

    def __init__(self, temporary_mp3_file: str = "temp.mp3") -> None:
        self.temporary_mp3_file = temporary_mp3_file

    def play(self, audio: bytes) -> None:
        """Play an audio file using pydub."""
        save_file(self.temporary_mp3_file, audio)
        self._play_mp3_file(self.temporary_mp3_file)
        delete_file(self.temporary_mp3_file)

    def _play_mp3_file(self, filename: str) -> None:
        speech = AudioSegment.from_mp3(filename)
        play(speech)
