from django.contrib import admin
from stockpost.models import StockPosts, Contact, comments
# Register your models here.

admin.site.register(Contact)
admin.site.register(StockPosts)
admin.site.register(comments)
