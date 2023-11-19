from app.views import *
from django.urls import path

urlpatterns = [
    path("", hello),
    path("job/<id>", job_detail),
]
