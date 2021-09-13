from celery  import Celery

app = Celery("Calculator" , broker = "amqp://guest:guest@localhost:5672//")

app.conf.task_default_exchange = "Calculator"
app.conf.task_default_routing_key = "Calculator"
app.conf.task_default_queue = "Calculator"

@app.task()
def calculate(a , b):
    print('1) + /n2) - /n3) / /n4) * ')
    choice = int(input("Enter your choice"))
    if choice == 1 : return a + b
    if choice == 2 : return a - b
    if choice == 3 : return a//b
    if choice == 4 : return a * b
    else : print("Invalid choice") ; return 

