from django.contrib import admin
from .models import Categories, Authors, Languages, Books, BookAuthor, Reviews
# Register your models here.

admin.site.register(Authors)
admin.site.register(Categories)
admin.site.register(Books)
admin.site.register(BookAuthor)
admin.site.register(Reviews)
admin.site.register(Languages)