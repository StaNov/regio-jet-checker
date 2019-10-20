import os
import tempfile
import time

from gtts import gTTS
from pygame import mixer


def say(to_say):
    tts = gTTS(to_say)
    tts.lang = "cs"

    try:
        f = tempfile.NamedTemporaryFile(delete=False)
        temp_file_name = f.name
        f.close()

        tts.save(temp_file_name)

        mixer.init()
        mixer.music.load(temp_file_name)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)
    finally:
        f.close()
        os.unlink(temp_file_name)


if __name__ == '__main__':
    say("Jde chleba a potká chleba s máslem")
