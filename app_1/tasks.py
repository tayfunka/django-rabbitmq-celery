from celery.utils.log import get_task_logger

from project.celery import app
from .email import send_review_email


logger = get_task_logger(__name__)


@app.task
def send_review_email_task(name, email, review):
    logger.info(f"Email sent to {name} at {email}.")
    return send_review_email(name, email, review)


@app.task
def add(x, y):
    logger.info(f"Adding {x} and {y}.")
    return x + y
