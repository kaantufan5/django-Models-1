from django.urls import path
from fscohort.views import home, starter


urlpatterns = [
    path('home/', home),
    path('', starter)
]