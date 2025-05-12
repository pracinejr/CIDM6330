from celery import Celery

Broker_URL = "redis://localhost:6379/0"
Backend_URL = "redis://localhost:6379/1"

app = Celery("tasks", broker=Broker_URL, backend=Backend_URL)


@app.task
def add(x, y):
    print(f"Adding {x} and {y}")
    return x + y


@app.task
def multiply(x, y):
    print(f"Multiplying {x} and {y}")
    return x * y
