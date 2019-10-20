import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

URL = (
    "https://shop.regiojet.cz"
    "?locale=cs"
    "&departureDate=2019-11-01"
    "&fromLocationId=10202002"
    "&toLocationId=10202003"
    "&fromLocationType=CITY"
    "&toLocationType=CITY"
    "&tariffs=REGULAR"
    "&tariffs=REGULAR"
    "&tariffs=ATTENDED_CHILD"
    "&tariffs=ATTENDED_CHILD"
)


def get_available_trains():
    with webdriver.Firefox() as ff:
        return _get_available_trains_info(ff)


def _get_available_trains_info(ff):
    ff.get(URL)

    while True:
        try:
            ff.find_element_by_class_name("routes")
            break
        except NoSuchElementException:
            time.sleep(0.5)

    wrappers = ff.find_elements_by_css_selector(".routes > div > div.connection-detail")

    wrappers = list(filter(_is_train_wrapper, wrappers))
    available_trains_info = list(map(_wrapper_to_info, wrappers))

    return list(filter(
        lambda train_info: int(train_info.departure_time.split(":")[0]) >= 7,
        available_trains_info
    ))


def _wrapper_to_info(wrapper: WebElement):
    departure_time = _get_departure_time(wrapper)

    wrapper.find_element_by_css_selector(".price button.yellow").click()

    while True:
        try:
            sections_wrap = wrapper.find_element_by_class_name("sections-wrap")
            break
        except NoSuchElementException:
            time.sleep(0.1)

    standard_class_seats = sections_wrap.find_elements_by_css_selector(".seats")[1].text

    return AvailableTrainInfo(departure_time, standard_class_seats)


def _is_train_wrapper(wrapper: WebElement):
    train_wraps = wrapper.find_elements_by_css_selector("[data-original-title=\"Vlak\"]")
    return len(train_wraps) > 0


def _get_departure_time(wrapper: WebElement):
    return wrapper.find_element_by_css_selector(".times > span:first-child > span").text


class AvailableTrainInfo:
    def __init__(self, departure_time, free_seats):
        super().__init__()
        self.departure_time = departure_time
        self.free_seats = free_seats

    def __str__(self) -> str:
        return (
            "AvailableTrainInfo("
            f"time={self.departure_time}, "
            f"seats={self.free_seats})")

    __repr__ = __str__


if __name__ == '__main__':
    trains = get_available_trains()
    print(str(trains))
