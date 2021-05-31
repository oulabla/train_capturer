
from flask import Flask
from celery import Celery

app = Flask(__name__)
worker_app = Celery('worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.route('/start_task')
def call_method():
    app.logger.info("Invoking Method ")
    #                        queue name in task folder.function name
    r = worker_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    app.logger.info(r.backend)
    return r.id


@app.route('/task_status/<task_id>')
def get_status(task_id):
    status = worker_app.AsyncResult(task_id, app=worker_app)
    
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@app.route('/task_result/<task_id>')
def task_result(task_id):
    result = worker_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)