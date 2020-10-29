# Sample flask app with a background worker

## Setup
```
$ mkvirtualenv flask-app
$ pip install flask gunicorn rq
```

## Start the flask app
```
$ gunicorn -b 0.0.0.0:5000 main:app --workers 2
$ tail -f app.log
```

## Start the workers
```
$ python worker.py
$ tail -f worker.log
```

## Credits
Miguel Grinberg's blog https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure