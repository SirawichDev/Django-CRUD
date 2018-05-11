from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=10)
    Comment = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
# แปลง object->string
    # def __unicode__(self):
    #     return self.title

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        #ids =>พารามิเตอร์ของ go_to_detail
        return reverse("posts:detail",kwargs={"ids": self.id})

    # def get_list(self):
    #     return reverse("posts:ShowList",kwargs={"ids": self.id})