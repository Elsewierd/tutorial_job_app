from app.views import hello, job_detail
from django.urls import path

urlpatterns = [
    path("", hello),
    path("job/1", job_detail),
]
