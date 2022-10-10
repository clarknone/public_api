import os
import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from helper.generator import Generator


def get_image_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return "blog/post/%s.%s" % (secrets.token_hex(32), file_extension)


# Create your models here.

class BaseModel(models.Model):
    id = models.PositiveIntegerField(default=Generator.generate_pk, primary_key=True, blank=True)
    date = models.DateTimeField(default=now, blank=True)

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=1024)
    image = models.ImageField(upload_to=get_image_path, max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
