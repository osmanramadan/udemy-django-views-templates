from django.db import models
from django.conf import settings

# Create your models here.

user = settings.AUTH_USER_MODEL

class Blog(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50,unique=True)
    content = models.TextField(null=True, blank=True)
    #image = models.ImageField(upload_to='photos/%y/%m/%d')
    #active = models.BooleanField(default=True)
    #category = models.CharField(max_length=50, null=True, blank=True,choices=[('phone','phone'),('laptop','laptop'),('tablet','tablet')])

    def __str__(self):
        return self.name
    
    #class Meta:
      #  verbose_name_plural = 'Blogs'
        