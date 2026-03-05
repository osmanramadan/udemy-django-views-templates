from django.db import models
from django.conf import settings
from pytz import timezone

# Create your models here.

user = settings.AUTH_USER_MODEL


    


class Blog(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50,unique=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=False,auto_now=False,null=True, blank=True)
    
   # timestamp = models.DateTimeField(auto_now_add=True)
   # updated_date = models.DateTimeField(auto_now=True)

    #image = models.ImageField(upload_to='photos/%y/%m/%d')
    #active = models.BooleanField(default=True)
    #category = models.CharField(max_length=50, null=True, blank=True,choices=[('phone','phone'),('laptop','laptop'),('tablet','tablet')])

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_update_url(self):
        return f"/blog-update/{self.slug}"
    
    def get_delete_url(self):
        return f"/blog-delete/{self.slug}"
    
    def get_create_url(self):
        return f"/blog-create/"
    
    def get_details_url(self):
        return f"/blog/{self.slug}"
    
    #class Meta:
      #  verbose_name_plural = 'Blogs'
        