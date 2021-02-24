from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Techblog(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=300)
    url = models.TextField(default="")
    image = models.ImageField(null=True)
    date = models.DateField()
    Directory = models.ForeignKey(Techblog, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title
