from django.db import models
from django.utils.text import slugify

# Create your models here.
class Services(models.Model):
    Title = models.CharField(max_length=256)
    Caption = models.CharField(max_length=256)
    Details = models.TextField()
    slug = models.SlugField(unique=True,  allow_unicode=True, blank=True)
    image = models.ImageField(upload_to='service_images/', height_field=None, width_field=None, max_length=None, null=True)
    online = models.BooleanField(default=False)
    Show_on_website = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.Title)
        super(Services,self).save(*args,**kwargs)

    def __str__(self):
        return self.Title

    
    
