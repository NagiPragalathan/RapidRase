from django.db import models
import uuid

class Details(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    detailsTitle = models.CharField(max_length=255)
    description = models.TextField()
    points = models.CharField(max_length=255)  # Changed from IntegerField to CharField
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)

class DetailsImage(models.Model):
    details = models.ForeignKey(Details, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')  # Each instance represents a single image

    def __str__(self):
        return f"Image for {self.details.uuid}"




