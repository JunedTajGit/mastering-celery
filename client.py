import time

# client is use to submit a task and get the answer.

# AsyncResult is use to create a object to get result and query the result.
from celery.result import AsyncResult

from worker import random_number, app

time.sleep(5)

# this is a way to call task
# this is provide a promise that will contain result.
result_future = random_number.delay(100)
result = AsyncResult(result_future.id, app=app)

print("Submitted Task")


# show the current state of result
print(result.result)

while True:
    if result.ready():
        print(result.get())
        break
    else:
        print(result.state)
        time.sleep(1)
