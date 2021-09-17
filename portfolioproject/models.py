from django.db import models

# Create your models here.from django.db import models
from datetime import date

from django.db.models.fields import EmailField

# Create your models here.

class Contact(models.Model):
    cname = models.CharField(max_length=50)
    cmessage = models.TextField()
    cemail = models.EmailField()
    csubject = models.TextField()



    
