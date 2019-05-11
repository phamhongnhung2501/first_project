from django.conf import settings
from django.db import models
from django.utils import timezone
# chỉ ra đây là 1 object
# class: từ khóa dùng để xác định một đối tượng
# Post: là tên của model, có thể đặt tên khác nhưng phải luôn bắt đầu bằng một chữ viết hoa
# models.Model: Post là model của Django, vì vậy Django biết nó nên được luư trong CSDL
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # xác định văn bản với số lượng ký tự giới hạn
    title = models.CharField(max_length=200)
    # đây là cho văn bản dài mà không có giới hạn
    text = models.TextField()
    # models.DateTimeField - là một ngày và thời gian 
    created_date = models.DateTimeField(default=timezone.now)
    # models.ForeignKey - là một liên kết đến một mô hình khác 
    published_date = models.DateTimeField(blank=True, null=True)
    # hàm publish thời gian
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # hàm trả về title 
    # note: khi viết các hàm phải thụt vào 4 space
    def __str__(self):
        return self.title