import time
from celery.result import AsyncResult

from LLMWorker import movie_info, app

time.sleep(5)


result_future1 = movie_info.delay("Tell me about the moviee shutter island")
result_future2 = movie_info.delay("Tell me about the moviee Inception")
result_future3 = movie_info.delay("Tell me about the moviee Predestination")

result_futures = [result_future1, result_future2, result_future3]

results = [AsyncResult(rf.id, app=app) for rf in result_futures]

print(
    "We can Immediately proceed with the remaining programming logic and don't need to wait for completion"
)

while True:
    if not results:
        break

    for r in results:
        # if r.state == 'Success'

        if r.ready():
            print(r.get())
            results.remove(r)

    time.sleep(1)
