#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Celery主类
启动文件名必须为celery.py！！！
"""

from __future__ import absolute_import  # 为兼容Python版本
from celery import Celery, platforms

platforms.C_FORCE_ROOT = True  # linux环境下，用于开启root也可以启动celery服务，默认是不允许root启动celery的
app = Celery(
    main='celery_tasks',  # celery启动包名称
    # broker='redis://localhost',
    # backend='redis://localhost',
    include=['celery_tasks.tasks', ]  # celery所有任务
)
app.config_from_object('celery_tasks.config')  # celery使用文件配置

if __name__ == '__main__':
    app.start()