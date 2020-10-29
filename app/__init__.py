from flask import Flask
import logging
from redis import Redis
import rq

def create_app():
    app = Flask(__name__)
    logging.basicConfig(filename='app.log', format='%(asctime)s : %(levelname)s : %(name)s : %(thread)d : %(process)d : %(message)s', level=logging.DEBUG)
    app.task_queue = rq.Queue('microblog-tasks', connection=Redis.from_url('redis://'))

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    app.logger.info("started app")
    return app