from django.db import models

# Create your models here.
class Services(models.Model):
    Title = models.CharField(max_length=256)
    Caption = models.CharField(max_length=256)
    Details = models.CharField(max_length=1256)
    models.ImageField(upload_to='service_images/', height_field=None, width_field=None, max_length=None)
    online = models.BooleanField(default=False)
    Show_on_website = models.BooleanField(default=False)

    
    
