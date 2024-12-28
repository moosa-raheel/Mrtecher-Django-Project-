from django.urls import path
from resume.views import Resume

urlpatterns = [
    path("upload/",Resume.as_view(),name="resume_upload")
]
