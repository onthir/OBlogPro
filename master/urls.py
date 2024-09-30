from django.urls import path, re_path
from . import views

app_name = 'master'
urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    re_path(r'^blog/(?P<slug>.+)/$', views.details, name='details'),  # Regex for blog slug
    re_path(r'^topic/(?P<cat>.+)/$', views.filter, name='filter'),  # Regex for category filter
    re_path(r'^archive/(?P<date>.+)/$', views.archive, name='archive'),  # Regex for date-based archive
    path('contact/', views.contact, name='contact'),  # Standard contact URL
    path('panel/', views.admin_panel, name='panel'),  # Standard admin panel URL
    re_path(r'^readnotf/(?P<id>\d+)/$', views.read_notification, name='readnotf'),  # Regex for notification ID
    re_path(r'^remove/message/(?P<id>\d+)/$', views.remove_message, name='remove_message'),  # Regex for message removal by ID
    re_path(r'^remove/notification/(?P<id>\d+)/$', views.remove_notf, name='remove_notf'),  # Regex for notification removal by ID
    re_path(r'^google1178e9883bf5717c\.html$', views.google_verification, name='google')  # Google verification file URL
]
