from django.contrib import admin

# from sport_shop.applications.account.models import CustomUser
from .models import CustomUser

admin.site.register(CustomUser)
