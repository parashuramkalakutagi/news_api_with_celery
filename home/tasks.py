import random

from celery import shared_task
from datetime import timedelta
# from datetime import timezone
from django.utils import timezone
from .NewsApiData import jaurnal,News_data





@shared_task(bind= True)
def news_api(self):
    jaurnal()
    return " jurnal api called successfully...."


@shared_task(bind= True)
def business_api(self):
    News_data()
    return " news  api called successfully...."