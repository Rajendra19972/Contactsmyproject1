from django.contrib import admin
from .models import details
# Register your models here.
class detailsadmin(admin.ModelAdmin):
    list_display = ['id','avatar','first_name','last_name','phonenumber','email','company','job_title']

admin.site.register(details,detailsadmin)
