from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apply/for/leave$', views.applying_for_leave, name='leave_application'),

]
