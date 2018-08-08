from django.contrib import admin
from .models import Post


# To make the model visible on the admin page, register the model with admin.site.register(Post)
admin.site.register(Post)