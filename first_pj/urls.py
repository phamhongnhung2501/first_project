from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Dòng này có nghĩa là với mỗi URL bắt đầu bằng admin/, Django sẽ tìm thấy chế độ xem tương ứng 
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
