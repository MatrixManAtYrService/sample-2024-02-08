import json
from datetime import date
from pathlib import Path

from pydantic import BaseModel
from typer import Typer


# we will be storing these objects in a text file
# we're using pydantic to handle the conversion between text and python objects
# it will be serialized in a language called json

class Meal(BaseModel):
    name: str
    calories: int


class Drink(Meal):
    # (one drink equivalent)
    num_ode: int


class TrackedDay(BaseModel):
    meals: list[Meal] = []
    drinks: list[Drink] = []


class History(BaseModel):

    by_date: dict[str, TrackedDay] = {}

    # date objects are not json serializable, so we're using strings instead
    # this lets the caller still query by date object
    def get_day(self, day: date) -> TrackedDay:
        return self.by_date[day.isoformat()]

# we want to be able to write tests without cluttering up the test-runner's directory
# the 'Data' class lets the test inject its own path
# outsitde of test, trackapp will just use the current working directory

class Data:
    def __init__(self, db_path: Path | None = None):
        if db_path:
            self.db = db_path
        else:
            self.db = Path.cwd() / "trackapp.json"

    def read(self) -> History:
        if not self.db.exists():
            print(f"{self.db} not found, assuming day 1")
            return History(by_date={})
        else:
            return History.model_validate_json(self.db.read_text())

    def write(self, history: History) -> None:
        if self.db.exists():
            verb = "updated"
        else:
            verb = "wrote"

        self.db.write_text(json.dumps(history.model_dump(), indent=2))
        print(verb + str(self.db.absolute()))


def add(on_day: date, data: Data, thing: Meal | Drink) -> None:
    history = data.read()
    today = history.by_date.setdefault(on_day.isoformat(), TrackedDay())

    if isinstance(thing, Meal):
        today.meals.append(thing)
    elif isinstance(thing, Drink):
        today.drinks.append(thing)
    else:
        raise TypeError(f"Whats a {type(thing)}?")

    data.write(history)


# we're using typer as a bridge between the CLI world and our python app
# $ trackapp --help
# $ trackapp add-meal --help
# $ trackapp add-meal shake 1000

app = Typer()


@app.command()
def add_meal(name: str, calories: int):
    data = Data()
    meal = Meal(name=name, calories=calories)
    add(date.today(), data, meal)


@app.command()
def add_drink(name: str, calories: int, num_ode: int):
    data = Data()
    drink = Drink(name=name, calories=calories, num_ode=num_ode)
    add(date.today(), data, drink)


def cli():
    app()
