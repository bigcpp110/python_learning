from __future__ import absolute_import
from celery import Celery, group
from .celery import app
from time import sleep


@app.task
def add(x, y):
    sleep(5)
    return x + y


@app.task
def substract(x, y):
    sleep(5)
    return x - y