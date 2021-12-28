from django.db import models


class Tasks(models.Model):
    username = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=255, blank=False)
    attached_file = models.FileField(blank=True)

    def __str__(self):
        return self.name