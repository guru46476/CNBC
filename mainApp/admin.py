from django.contrib import admin
from .models import Contect
# Register your models here.

@admin.register(Contect)
class ContectAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','status']

# second method to register your site:--------------------------->

# admin.site.register((
#     Contect,
# ))