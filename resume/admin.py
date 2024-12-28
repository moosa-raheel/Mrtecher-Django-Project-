from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','address','gender','state','prefered_location','profile_image','resume_file']