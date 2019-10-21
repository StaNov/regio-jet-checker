import mmap
import os
import tempfile
import time

from gtts import gTTS
from pygame import mixer


def say(to_say):
    tts = gTTS(to_say)
    tts.lang = "cs"

    with tempfile.NamedTemporaryFile() as f:
        tts.save(f.name)
        file_to_play = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    mixer.init()
    mixer.music.load(file_to_play)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)


if __name__ == '__main__':
    say("Jde chleba a potká chleba s máslem, \n\n" * 3)
