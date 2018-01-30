from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index1, name='index1'),
    url(r'^index1.html$', views.index1, name='index1'),
    url(r'^output1.html$', views.output1, name='output1'),
    url(r'^input1.html$', views.input1, name='input1'),
    url(r'^download1.html$', views.download1, name='download1'),
    url(r'^acquire1.html$', views.acquire1, name='acquire1'),
    url(r'^page1.html$', views.page1, name='page1'),
    url(r'^page2.html$', views.page2, name='page2'),
    url(r'^work$', views.work),
    url(r'^download$', views.download),
    url(r'^tasks$', views.tasks),
    url(r'^acquire$', views.acquire),
]