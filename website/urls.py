from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('events/', views.events, name='events'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('notices/', views.notices, name='notices'),
    path('notices/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:pk>/', views.gallery_album, name='gallery_album'),
    path('achievements/', views.achievements, name='achievements'),
    path('alumni/', views.alumni, name='alumni'),
    path('alumni/<int:pk>/', views.alumni_detail, name='alumni_detail'),
    path('contact/', views.contact, name='contact'),
]
