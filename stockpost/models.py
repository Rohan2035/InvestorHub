from django.db import models
from django.db.models import DateField
# from django.contrib.auth.models import User

# StockPost Model
class StockPosts(models.Model):
    post_id = models.AutoField(primary_key = True)
    slug = models.CharField(max_length=50, default=None)
    Name = models.CharField(max_length=50, default=None)
    author = models.CharField(max_length=50, default = None)
    content = models.TextField(default=None)
    date = DateField(auto_now_add=True)
    img1 = models.ImageField(null=True,upload_to = "images")

    def __str__(self):
        return self.Name

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length = 100)
    Queries = models.TextField(default=None)

    def __str__(self):
        return self.name

# Comment Section
class comments(models.Model):
    post_id = models.ForeignKey(StockPosts, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=50, default=None)
    user_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.user_name



