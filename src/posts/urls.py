from django.conf.urls import url
from .views import (
    go_to_list
    go_to_create
    go_to_detail
    go_to_update
    go_to_delete
)
urlpatterns = [
    url(r'^$', go_to_list),

    url(r'^create/$',   go_to_create),

    url(r'^detail/$',    go_to_detail),

    url(r'^update/$',  go_to_update),

    url(r'^delete/$',   go_to_delete),
    #  url(r'^post/$', "posts.views.posts_home"),
]