from celery import Celery

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

celery.conf.task_default_queue = 'painter_queue'