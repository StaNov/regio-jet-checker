import tempfile
import time

from gtts import gTTS
from pygame import mixer


def say(to_say):
    tts = gTTS(to_say)
    tts.lang = "cs"

    with tempfile.NamedTemporaryFile() as f:
        tts.save(f.name)

        mixer.init()
        mixer.music.load(f)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(1)


if __name__ == '__main__':
    say("Jde chleba a potká chleba s máslem, a chleba s máslem povídá, chlebe, můžu jít s tebou? Přičemž chleba odpoví, jo můžeš, Takže jde chleba, chleba s máslem a potká chleba s máslem se salámem")
