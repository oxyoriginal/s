from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    short_name = models.CharField(max_length=20)
    about = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=False, blank=False )
    date = models.DateField(default=datetime.date.today)
    price = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    user = models.ForeignKey('auth.User', default=1, on_delete=models.CASCADE, verbose_name='user')
    image = models.ImageField(upload_to='s_app/img/', default='static/s_app/img/default.jpg')
    def __str__(self):
        return self.title


