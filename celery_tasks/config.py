#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_RESULT_BACKEND='redis://localhost:6379/1'
# BROKER_URL='redis://localhost:6379/2'
BROKER_BACKEND = 'mongodb'  # mongodb作为任务队列（或者说是缓存）
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'mongodb://localhost:27017/for_celery'  # 消息结果存储地址
CELERY_MONGODB_BACKEND_SETTINGS = {  # 消息结果存储配置
    'host': 'localhost',
    'port': 27017,
    'database': 'for_celery',
    # 'user':'root',
    # 'password':'root1234',
    'taskmeta_collection': 'task_meta',  # 任务结果的存放collection
}
CELERY_ROUTES = {  # 配置任务的先后顺序
    'celery_task.tasks.add': {'queue': 'for_add', 'router_key': 'for_add'},
    'celery_task.tasks.subtract': {'queue': 'for_subtract', 'router_key': 'for_subtract'}
}