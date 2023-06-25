from django.contrib import admin
from .models import *

admin.site.register(Purpose)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Comment)