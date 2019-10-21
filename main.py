from datetime import datetime
import time

import sayer
import webbrowser

SLEEP_IN_MINUTES = 20


def main():
    while True:
        trains = webbrowser.get_available_trains()
        _process_trains(trains)
        time.sleep(60 * SLEEP_IN_MINUTES)


def _process_trains(trains: [webbrowser.AvailableTrainInfo]):
    print(f"{datetime.now().replace(microsecond=0)} Available trains: {trains}")
    text_to_say = _trains_to_text(trains) + f"Konec hlášení, ozvu se zase za {SLEEP_IN_MINUTES} minut."
    sayer.say(text_to_say)


def _trains_to_text(trains):
    if not trains:
        return "Dávám vědět, že na RegioJet nejsou žádná volná místa. \n\n"

    text_to_say = f"Pozor pozor, jsou dostupné jízdenky na RegioJet. Celkem do {len(trains)} vlaků. \n\n"

    for i, train in enumerate(trains):
        text_to_say += f"Vlak číslo {i + 1}: Odjíždí v {train.departure_time} a je v něm {train.free_seats} volných míst. \n\n"

    return text_to_say


if __name__ == '__main__':
    main()
