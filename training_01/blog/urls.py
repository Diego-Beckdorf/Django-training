from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post, name='post'),
    url(r'^new_post/$', views.new_post, name='new post'),
    url(r'^my_posts/$', views.my_posts, name='my posts'),
    url(r'^logout/$', views.logout_view, name='logout'),
]