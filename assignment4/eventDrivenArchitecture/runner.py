from tasks import add
from tasks import multiply

# app = Celery("tasks", broker="redis://localhost:6379/0")
if __name__ == "__main__":
    result = add.delay(4, 13)
    result2 = multiply.delay(4, 13)
    print(
        f"Task {result2} has been sent: READY? {result2.ready()} STATUS: {result2.status}"
    )
    print(
        f"Task {result} has been sent: READY? {result.ready()} STATUS: {result.status}"
    )
    print(f"Added Numbers = {result.get()}, Multiplied numbers = {result2.get()}")
