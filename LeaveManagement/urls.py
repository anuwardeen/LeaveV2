from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apply/for/leave$', views.applying_for_leave, name='leave_application'),
    url(r'^respond/to/leave$', views.responding_to_leave_application, name='responding_to_leave'),

]
