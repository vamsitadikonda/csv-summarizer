## Requirements and Instructions
Specifies all requirements to implement the Summarizer package

Prerequisites

* [Python](https://www.python.org)

Upgrade pip:
```
python -m pip install --upgrade pip;
```
To clone the project from the repository:
```
git clone git@github.com:vamsitadikonda/csv-summarizer.git
```

Install all required packages for the repo:
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi;

After installing all the dependencies:

You can run the code:
```
python run.py [OPTIONS]
```

OPTIONS:
```
    -e  --eg        start-up example                        = None
    -d  --dump      on test failure, exit with stack dump   = False
    -f  --file      file with csv data                      = ../data/auto93.csv
    -h  --help      show help                               = False
    -n  --nums      number of nums to keep                  = 512
    -s  --seed      random seed                             = 10019
    -S  --Seperator field separator                         = ,
```

To run the tests
```bash
# Output is printed on the terminal
python run.py -e ALL
```
