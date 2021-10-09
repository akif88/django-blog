from django.contrib import admin
from .models import *


class AllAdmin(admin.ModelAdmin):
    pass

admin.site.register(Menu, AllAdmin)
admin.site.register(Post, AllAdmin)
admin.site.register(Tag, AllAdmin)
admin.site.register(Category, AllAdmin)
admin.site.register(Slider, AllAdmin)
admin.site.register(Hit, AllAdmin)
admin.site.register(Users, AllAdmin)
admin.site.register(Comment, AllAdmin)
admin.site.register(Feature, AllAdmin)
admin.site.register(Images, AllAdmin)
admin.site.register(Templates, AllAdmin)
admin.site.register(Pages, AllAdmin)
admin.site.register(Blog, AllAdmin)
admin.site.register(Content, AllAdmin)
admin.site.register(Account, AllAdmin)
admin.site.register(Author, AllAdmin)
admin.site.register(Reader, AllAdmin)
admin.site.register(IPLog, AllAdmin)
