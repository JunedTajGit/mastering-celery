import os
import time
import random

from celery import Celery

app = Celery(
    "random_number",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_BACKEND_URL"),
)

"""'
RABBITMQ_USER=customuser
# RABBITMQ_PASS=

CELERY_BROKER_URL=amqp://customuser:custompassword@rabbitmq:5672//
CELERY_BACKEND_URL=redis://redis:6379

REDIS_HOST = local:redis:6379

api_version="2024-12-01-preview"

AZURE_OPENAI_ENDPOINT=""

# AZURE_OPENAI_API_KEY=""
model_name = "gpt-4.1-mini"

"""


# task can be a long running process, like API call, Database , Email etc.
@app.task
def random_number(max_value):
    time.sleep(5)
    return random.randint(0, max_value)
