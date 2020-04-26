from django.contrib import admin
from blog1app.models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','body','publish','created','updated','status']
    list_filter=('status','created','author','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    orderning=['status','publish']
    prepopulated_fields={'slug':('title',)}

class commentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=['active','created','updated']
    search_fields=['name','email','body']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,commentAdmin)
