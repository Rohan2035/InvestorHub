from django.contrib import admin
from stockpost.models import StockPosts, Contact, PostComment
# Register your models here.

admin.site.register((StockPosts, PostComment))
admin.site.register(Contact)
