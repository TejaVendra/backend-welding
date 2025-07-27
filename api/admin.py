from django.contrib import admin
from .models import WorkImage
from .models import DesignOrder

admin.site.register(DesignOrder)
# Register your models here.
admin.site.register(WorkImage)