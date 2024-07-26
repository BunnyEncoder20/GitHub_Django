from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiTable(models.Model):
    
    CHAI_TYPE_CHOICES = [
        ('ml','Masale Tea'),
        ('gr','Ginger Tea'),
        ('ki','Kiwi Tea'),
        ('pt','Plain Tea'),
        ('eh','Elachi Tea'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_images/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    
    def __str__(self):
        return self.name
    