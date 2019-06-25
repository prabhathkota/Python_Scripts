"""
broker
    RabbitMQ we started earlier
    For RabbitMQ, the transport is amqp. (Advanced Message Queuing Protocol)
    The Advanced Message Queuing Protocol (AMQP) is an open standard application layer protocol for
        message-oriented middleware.
backend
    rpc means sending the results back as AMQP messages, which is an acceptable format for our demo

include
    The include argument specifies a list of modules that you want to import when Celery worker starts.
    We add the tasks module here so that the worker can find our task.
"""

from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://prabhath:prabhath123@localhost/prabhath_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
