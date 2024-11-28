import os
from celery import Celery
from app_name.tasks import add

# Django의 기본 설정을 Celery에서 사용하도록 등록
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')

# Celery 앱 생성
app = Celery('sample')

# Django 의 settings.py 파일에서 Celery 관련 설정을 가져옴
app.config_from_object('django.conf:settings', namespace='CELERY')

# Django의 앱에서 task를 자동으로 찾음
app.autodiscover_tasks(['app_name']) # task는 일반적으로 Celery와 같은 작업 큐를 사용하여 백그라운드에서 실행되는 비동기 작업을 의미
app.tasks.register(add)

@app.task(bind=True)
def debug_task(self):
	print(f'Request: {self.request!r}')