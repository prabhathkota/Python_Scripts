"""
Start Redis
    redis-server
Start RQ (Redis Queue)
    rq worker
python redis_queue_worker.py

Celery Vs RQ
    RQ is designed to be simpler all around.
    Celery is designed to be more robust.
"""

from rq import Queue
from redis import Redis
from redis_queue_test import count_words_at_url
import time

# Tell RQ what Redis connection to use
redis_conn = Redis(host='localhost', port=6379, db=0)
q = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(count_words_at_url, 'http://google.com')
print(job.result)   # => None

# Now, wait a while, until the worker is finished
time.sleep(2)
print(job.result)   # => 311


