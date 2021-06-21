from django.db import models


class Post(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey("src.v1.models.user.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['created']
