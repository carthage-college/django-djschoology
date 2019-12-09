from django.conf.urls import url

from djschoology.dashboard import views

urlpatterns = [
    url(
        r'^$',
        views.home, name='home'
    ),
]
