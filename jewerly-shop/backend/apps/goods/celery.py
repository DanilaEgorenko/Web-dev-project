from celery import Celery, shared_task

app = Celery('tasks', broker='redis://redis:6379/0')

@shared_task
def add(x, y):
    print("hi")
    return x + y

def get_celery_worker_status():
    i = app.control.inspect()
    availability = i.ping()
    stats = i.stats()
    registered_tasks = i.registered()
    active_tasks = i.active()
    scheduled_tasks = i.scheduled()
    result = {
        'availability': availability,
        'stats': stats,
        'registered_tasks': registered_tasks,
        'active_tasks': active_tasks,
        'scheduled_tasks': scheduled_tasks
    }
    return result