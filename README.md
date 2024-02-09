# Trackapp

This project doesn't do anything currently, come back later.

## Tooling

First go install poetry: https://python-poetry.org/

You'll know it works when you can do something like this (don't worry too much about the version number)

```
$ poetry --version
    Poetry (version 1.7.1)
```

To walk through a dev workflow
```
git clone https://github.com/MatrixManAtYrService/trackapp.git
cd trackapp
poetry install --with dev
poetry run pytest  # watch tests run
poetry run trackapp # watch trackapp run
```


To pretent you're a user:

```
# make a venv
python -m venv foo

# enter it
source foo/bin/activate

# install trackapp
pip install /path/to/trackapp

# run trackapp
trackapp

# leave the venv
deactivate
```

## Poetry, Venv, Huh?

It's best to avoid installing random python stuff in your system.
Eventually it becomes a very cluttered space and its hard to figure out why stuff doesn't work.
The solutin is these virtual environments.

The Poetry commands create a virtual envirionment just for that project and then run `pytest` and `trackapp` in that environment.
This is a nice way to develop because you don't end up relying on some "just on my machine" python package.

The `venv` command gave you a shell in the virtual environment, so you can sort of pretend that it's installed globally, even though it'll dissapear when you leave the environment.

Of course you can just run `pip install /path/to/trackapp` without a virtualenv at all, but the road to hell is paved with that sort of thing.
