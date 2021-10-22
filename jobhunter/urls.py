from django.urls import path

from . import views

app_name = "jobhunter"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_posting", views.add_posting, name="add_posting"),
    path("skills", views.skill_summary, name="skill_summary"),
    path("notes", views.notes, name="notes"),
    path("posting/<int:id>", views.posting, name="posting"),
    
    
    #API routes
    path("add/check", views.url_is_new, name="url_is_new"),
    path("skills/fetch", views.fetch_skills, name="fetch_skills")
]