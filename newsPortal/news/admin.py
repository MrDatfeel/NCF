from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment, Article, News

# Настройка админки для модели Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    search_fields = ('user__username',)

# Настройка админки для модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Настройка админки для модели Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'created_at', 'rating')
    list_filter = ('type', 'created_at')
    search_fields = ('title', 'author__user__username')
    #filter_horizontal = ('categories',)

# Настройка админки для модели PostCategory
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')
    list_filter = ('category',)
    search_fields = ('post__title',)

# Настройка админки для модели Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'rating')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'post__title')

# Настройка админки для модели Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ('title',)

# Настройка админки для модели News
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author')

# Регистрация моделей с настройками в админке
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)


