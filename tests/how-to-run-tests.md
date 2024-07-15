# HOW-TO: Running tests

A short how-to-guide to run tests written for the environment


## Prerequisits

* `coverage`-package -- testing framework which assist in understanding what coverage is gotten from the tests
* `live server`-VS Code extension -- this is the extension that enables you to interact with the `index.html`-file created by `coverage`

> ***NOTE***: To install `coverage` run the following command:
>
> `> pip install coverage`
>
>This can be run inside your python distro natively, or from within an activated conda environment.
>If either of the supplied `black_jack_requirments.txt` or `black_jack_environment.yml` files were used to do the `pip install` or `conda` environment creation respectively, this requirement will be met.

## Running <u>ALL</u> tests with `coverage`

If the prerequisits are met, then follow these steps to run the tests:

### 0. Setup

1. Ensure that your tests are saved in the `.\tests` directory
2. Ensure that all tests are named as follows `test_<class-to-be-tested>.py`

### 1. Run all tests

1. Ensure you are in the root directory of the project
2. Run:
```
> coverage run -m unittest discover
```

This will create a `.coverage`-file (which is a SQLite db)

### 2. Create html coverage report

1. Run:
```
> coverage html
```

This will produce a new directory `htmlcov` which contains (among other files) `index.html`

### 3. Open html coverage report

1. Right-click `index.html` file and select `Open with Live Server`

This opens the generated report, which allows you to navigate your code and the coverage of all tests

## Running specific tests with `coverage`

All setup and prerequists hold as for *all* tests. Simply run the following:

1. Ensure that you are in the root directory of your package
2. Run:
```
> coverage run -m unittest .\<tests-directory>\<name-of-test-to-run>.py
```

E.g.
```
> coverage run -m unittest .\tests\test_game.py
```


> ***NOTE***: this file is generated from a Windows perspective. It is assumed that Mac, and Linux will follow very similar steps.