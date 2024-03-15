from django.contrib import admin
from .models import Details, DetailsImage
from image_uploader_widget.widgets import ImageUploaderWidget
from django.db import models
# Register your models here.

@admin.register(DetailsImage)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }


admin.site.register(Details)
