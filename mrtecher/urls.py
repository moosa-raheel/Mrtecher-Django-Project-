from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("resume/", include("resume.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("base.urls")),

]
