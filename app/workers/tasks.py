# To test the worker execute following:  
# celery -A tasks worker --loglevel=info
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y