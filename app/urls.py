from app import views
from django.urls import path

urlpatterns = [
    path("", views.job_list, name="job_home"),
    path("job/<int:id>", views.job_detail, name="job_detail"),
]
