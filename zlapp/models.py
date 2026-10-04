from django.db import models

# Create your models here.

class News(models.Model):
    """最新消息。"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=30, null=True)
    author = models.CharField(max_length=30, null=True)
    cont = models.TextField()


    def __str__(self):
        """返回模型的字符串表示。"""
        return self.text

class Topic(models.Model):
    """网友留言主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)  # 点赞数

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.text

class Entry(models.Model):
    """网友评论的具体内容"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)  # 点赞数
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示。"""
        return f"{self.text[:50]}..."
