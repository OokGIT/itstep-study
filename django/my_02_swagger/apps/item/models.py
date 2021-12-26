from django.db import models


class Item(models.Model):

    title = models.CharField(max_length=20)
    url = models.URLField('url', max_length=500, blank=True, null=True, default=None)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
