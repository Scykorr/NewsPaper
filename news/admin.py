from django.contrib import admin
from .models import Post, PostCategory, Author, Category, Comment


def nullfy_post_rank(modeladmin, request, queryset):
    queryset.update(post_rank=0)


nullfy_post_rank.short_description = 'Обнулить ранк'


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'post_rank', 'author')

    list_filter = ('title', 'post_rank', 'author')

    search_fields = ('title', 'category__name')
    actions = [nullfy_post_rank]


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
