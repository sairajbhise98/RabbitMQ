from celery  import Celery

app = Celery("Demo_App" , broker = "amqp://guest:guest@localhost:5672//")

app.conf.task_default_exchange = "Demo_App"
app.conf.task_default_routing_key = "Demo_App"
app.conf.task_default_queue = "Demo_App"

@app.task()
def add_numbers(a , b):
    return a+b