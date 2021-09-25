from django.db import models

# Create your models here.


class TopicMain(models.Model):
    """用户发布的主题"""
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text