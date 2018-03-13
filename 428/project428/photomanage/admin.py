from django.contrib import admin

# Register your models here.
from models import Photos
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id','category','httpurl')
 
admin.site.register(Photos, PhotosAdmin) 
