import dataclasses
import datetime
from enum import Enum
import random

from faker import Faker

faker = Faker("ru_RU")


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    address: str
    station: str
    phone_number: str
    date_delivery: int
    rent_period: str
    bike_colour: str


class Station(Enum):
    # Red
    cherkizovskaya = "Черкизовская"
    sokolniki = "Сокольники"
    lubyanka = "Лубянка"
    # Green
    sokol = "Сокол"
    dinamo = "Динамо"
    tekhnopark = "Технопарк"
    # Blue
    mitino = "Митино"
    strogino = "Строгино"
    arbatskaya = "Арбатская"


class RentPeriod(Enum):
    one_day = "сутки"
    two_days = "двое суток"
    three_days = "трое суток"
    four_days = "четверо суток"
    five_days = "пятеро суток"
    six_days = "шестеро суток"
    seven_days = "семеро суток"


class BikeColour(Enum):
    grey = "grey"
    black = "black"


user = User(
    faker.first_name(),
    faker.last_name(),
    faker.city(),
    Station.sokol.value,
    faker.ssn(),
    (datetime.date.today() + datetime.timedelta(days=1)).day,
    RentPeriod.four_days.value,
    BikeColour.black.value
)
