from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from trackapp.app import Data, Meal, add


def test_one_drink():
    today = date.today()
    with TemporaryDirectory() as d:
        path = Path(d) / "trackapp.json"

        # write some stuff to an empty file
        # (like if the user ran the app for the first time)
        data = Data(path)
        add(today, data, Meal(name="shake", calories=1000))

        # read it from disk
        # (as if the user is calling the program a second time)
        new_history = data.read()

        # if you invoke pytest with -s, you can see print output
        # this shows the content of the file
        print(path.read_text())

    # is the data intact?
    assert len(new_history.get_day(today).drinks) == 0
    assert new_history.get_day(today).meals[0].name == "shake"
    assert new_history.get_day(today).meals[0].calories == 1000

        
