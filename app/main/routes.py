from app.main import bp
from flask import current_app

@bp.route('/')
@bp.route('/index')
def index():
    job = current_app.task_queue.enqueue('app.tasks.example', 5)
    current_app.logger.info('job id: ' + job.get_id())
    return job.get_id()