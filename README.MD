# Flask app with a background worker

## Setup
```
$ mkvirtualenv flask-app
$ pip install flask gunicorn rq
```

## Start the flask app
```
$ gunicorn -b 0.0.0.0:5000 main:app --workers 2
```

## Start the workers
```
$ python worker.py
```