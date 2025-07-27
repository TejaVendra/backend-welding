from django.db import models

# Create your models here.
# models.py
class WorkImage(models.Model):
    category = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return f"{self.category} - {self.image_url}"
# models.py

class DesignOrder(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    design_name = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.design_name}"
