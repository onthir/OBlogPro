from django.urls import path, re_path
from . import views

app_name = 'download'

urlpatterns = [
    path('', views.home, name='home'),  # Root URL for the home view
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),  # Regex for details view with numeric ID
]
