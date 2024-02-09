# Trackapp

This project doesn't do anything useful yet

## some Flows

First go install poetry: https://python-poetry.org/

You'll know it works when you can do something like this (don't worry too much about the version number):
```
$ poetry --version
    Poetry (version 1.7.1)
```

Then clone the code and enter the project diretory, and resolve dependencies:
```
git clone https://github.com/MatrixManAtYrService/trackapp.git
cd trackapp
poetry install --with dev
```


**A session where I use poetry to test the CLI**
```
poetry run trackapp add-meal shake 1000

    /Users/matt/src/trackapp/trackapp.json not found, assuming day 1
    wrote/Users/matt/src/trackapp/trackapp.json

poetry run trackapp add-meal shake 900

    updated/Users/matt/src/trackapp/trackapp.json

cat trackapp.json

    {
      "by_date": {
        "2024-02-08": {
          "meals": [
            {
              "name": "shake",
              "calories": 1000
            },
            {
              "name": "shake",
              "calories": 900
            }
          ],
          "drinks": []
        }
      }
    }
   
```

**Or run an automated test via pytest**

```
poetry run pytest -s

  ====== test session starts =====
  platform darwin -- Python 3.11.6, pytest-8.0.0, pluggy-1.4.0
  rootdir: /Users/matt/src/trackapp
  collected 1 item

  test/test_app.py /var/folders/2v/54n59bkd0ts6wlydrr66vlpm0000gn/T/tmp8vvmqe5t/trackapp.json not found, assuming day 1
  wrote/var/folders/2v/54n59bkd0ts6wlydrr66vlpm0000gn/T/tmp8vvmqe5t/trackapp.json
  {
    "by_date": {
      "2024-02-08": {
        "meals": [
          {
            "name": "shake",
            "calories": 1000
          }
        ],
        "drinks": []
      }
    }
  }
  .

  ===== 1 passed in 0.04s =====
```
  
That was just one test, but it's nice having them automated because later you may have hundreds of them.
It's quite nice to be able to run them all together in a way that doesn't change based on your ability to produce typos.
If you run them often between changes you will know when you've fixed the problem, or when you've broken something else.

**Let the Magic Begin**

Once you can do this relatively quickly, things start getting fun.
Until that point, maybe less fun.

1. tweak test, run tests
2. tweak code, run tests
3. repeat

This repo should already have you at that point.

Of course you have to figure out how to work with all of the new tools that I dumped on you.
And probaly my code was unfamilliar to you in some places (if not all places).
So uh... explore... ask questions... etc.

If you're feeling ambitious: Try to add a feature.
Maybe a command that adds the calories for today.

Or maybe go bug hunting.
Here's one:

```
rm trackapp.json

poetry run trackapp add-drink foo 2 3

  /Users/matt/src/trackapp/trackapp.json not found, assuming day 1
  wrote/Users/matt/src/trackapp/trackapp.json

cat /Users/matt/src/trackapp/trackapp.json

  {
    "by_date": {
      "2024-02-08": {
        "meals": [
          {
            "name": "foo",
            "calories": 2
          }
        ],
        "drinks": []
      }
    }
  }

```

It added my drink as a meal.  What's going on?

That's a real bug, by the way, I didn't put it in there for you, I made a mistake.
Then I spotted it and decided to leave my mistake there, because it's perhaps an instructional one.
It has to do with [isinstance](https://docs.python.org/3/library/functions.html#isinstance).
