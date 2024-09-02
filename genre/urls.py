# from django.urls import path
# from . import views

# urlpatterns = [
#     path('hello.html', views.index, name='hello'),
#     path('contact.html', views.contact, name='contact'),
#     path('service.html', views.service, name='service'),
#     path('about.html', views.about, name='about'),
#     path('guard.html', views.guard, name='guard'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='genre-home'),  # This will serve hello.html at /genre/
    path('hello.html', views.index, name='hello'),
    path('contact.html', views.contact, name='contact'),
    path('service.html', views.service, name='service'),
    path('about.html', views.about, name='about'),
    path('guard.html', views.guard, name='guard'),
]
