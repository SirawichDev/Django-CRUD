from django.conf.urls import url
from posts.views import go_to_home
urlpatterns = [
    url(r'^$', go_to_home,name="home"),
    #  url(r'^post/$', "posts.views.posts_home"),
]