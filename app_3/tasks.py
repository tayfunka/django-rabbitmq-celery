import sys
import json
from django.core.management import call_command
from django.core import serializers
from project.celery import app

from .models import Post
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def bkup():
    posts = Post.objects.all()
    logger.info(f"Backup of {len(posts)} posts.")

    with open('backup.json', 'w') as file:
        data = serializers.serialize('json', posts)
        file.write(data)
    logger.info("Backup completed.")
    return True
