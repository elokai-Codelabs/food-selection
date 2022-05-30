from django.db import models
import uuid

# Create your models here.
class Selections(models.Model):
    class_name = models.CharField(max_length=255, null=True,blank=True)
    meal_selected =  models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False,primary_key=True)

    def __str__(self):
        return self.class_name
    
