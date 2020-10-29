import rq
import logging
from redis import Redis

logger = logging.getLogger("rq.worker")
file_handler = logging.FileHandler('worker.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(thread)d : %(process)d : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

with rq.Connection(Redis.from_url('redis://')) as conn:
    qs = rq.Queue('microblog-tasks', connection=conn)
    w = rq.Worker(qs)
    w.work()