from django.conf.urls import url
from .views import (
    go_to_list
    go_to_create
    go_to_detail
    go_to_update
    go_to_delete
)
urlpatterns = [
    url(r'^$', views.go_to_list,name="list"),

    url(r'^create/$', views.go_to_create,name="create"),

    url(r'^detail/$', views.go_to_detail,name="detail"),

    url(r'^update/$', views.go_to_update,name="update"),

    url(r'^delete/$', views.go_to_delete,name="delete"),
    #  url(r'^post/$', "posts.views.posts_home"),
]