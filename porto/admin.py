from django.contrib import admin
from .models import fitur, education, experience, contact, project, setting 
# Register your models here.


    
admin.site.register(education),
admin.site.register(experience),
admin.site.register(fitur),
admin.site.register(contact),
admin.site.register(project)
admin.site.site_header = "FikWeb Admin Handsome"
admin.site.site_title = "Welcome to FikWeb Admin"
admin.site.index_title = "Fikweb admin"
admin.site.register(setting)