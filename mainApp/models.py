from django.db import models
from django.core.urlresolvers import reverse


class Area(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    photo = models.ImageField(upload_to='areas/', default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('areas-detail', args=[str(self.id)])


class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    time = models.CharField(max_length=20, help_text="How much time service will take")
    price = models.IntegerField()
    area = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])
