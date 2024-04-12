from .models import Author, Quote, Tag
from django.contrib import admin

# Register your models here.

admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(Tag)

