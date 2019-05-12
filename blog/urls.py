from django.urls import path
from . import views

urlpatterns = [
    # gán view gọi post_list cho URL gốc, URL này sẽ khớp với một chuỗi trống và trình phân giải URL Django sẽ bỏ qua tên miền
    # (ví dụ: http://127.0.0.1:8000/ ) có tiền tố đường dẫn url đầy đủ. Mẫu này sẽ cho Django biết đây views.post_listlà nơi thích hợp nếu ai đó truy cập trang web của bạn tại địa chỉ ' http://127.0.0.1:8000/ '. 
    # name='post_list', là tên của URL sẽ được sử dụng để xác định chế độ xem
    path('', views.post_list, name='post_list'),
]