from django.contrib import admin
from .models import Post
# Để hiển thị model của chúng tôi trên trang quản trị
admin.site.register(Post)