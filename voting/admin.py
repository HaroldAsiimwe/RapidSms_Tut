from django.contrib import admin
from .models import Choice

#file that is added to the Django admin site
#Registers models to the Admin Site 

admin.site.register(Choice)
