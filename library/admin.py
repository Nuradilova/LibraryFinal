from django.contrib import admin
from library.models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookBorrower)
admin.site.register(Borrower)
admin.site.register(Example)