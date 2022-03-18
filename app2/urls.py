from app2.views import a2_kohli
from django.urls import path
app_name='app2'
urlpatterns=[
    path('a2_kohli/',a2_kohli,name='a2_kohli'),
]