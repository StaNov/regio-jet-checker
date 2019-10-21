import tempfile
import time

import vlc
from gtts import gTTS


def say(to_say):
    tts = gTTS(to_say)
    tts.lang = "cs"

    with tempfile.NamedTemporaryFile() as f:
        tts.save(f.name)
        p = vlc.MediaPlayer("file://" + f.name)
        p.play()
        time.sleep(1)
        while p.is_playing():
            time.sleep(1)


if __name__ == '__main__':
    say("Jde chleba a potká chleba s máslem, \n\n" * 3)
