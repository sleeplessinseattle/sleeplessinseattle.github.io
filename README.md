## Setup

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Editing files
Edit files in the templates, static/css/src, static/js/src, and static/img directories. static/css and static/js and top level html files are generated using python freeze.

## Updating static files
```
python freeze.py
```

## Running dev webserver
```
python run.py
```
