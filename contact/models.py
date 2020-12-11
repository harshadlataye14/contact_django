from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    manager =models.ForeignKey(User,  on_delete=models.CASCADE,default=None)
    Name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    info = models.CharField(max_length=300)
    gender = models.CharField(max_length=50, choices=(
        ('male','Male'),
        ('female','Female')
    ))
    image = models.ImageField(upload_to="image/",blank=True )
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name
    