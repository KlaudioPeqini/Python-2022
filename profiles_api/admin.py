from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Student)
admin.site.register(models.Book)
admin.site.register(models.Users)
admin.site.register(models.BookType)
admin.site.register(models.Borrowers)
