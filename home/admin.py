from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Genres)
admin.site.register(Movies)
admin.site.register(admin_login)
admin.site.register(profile)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Watchlist)