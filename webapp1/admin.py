from django.contrib import admin

# Register your models here.
from .models import testmodel

admin.site.register(testmodel)
