from django.conf.urls import url
from .views import (
    go_to_list,
    go_to_home,
    go_to_create,
    go_to_detail,
    go_to_update,
    go_to_delete,
)
urlpatterns = [
    url(r'^index',go_to_home),
    url(r'^$', go_to_list),
    url(r'^create/$', go_to_create),
    url(r'^(?P<ids>\d+)/$', go_to_detail, name='detail'),
    url(r'^(?P<ids>\d+)/edit/$',  go_to_update ,name='update'),
    url(r'^delete/$',   go_to_delete),
    #  url(r'^post/$', "posts.views.posts_home"),
]