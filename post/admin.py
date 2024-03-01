from django.contrib import admin
from .models import Article, ArticleRating, Categories  # Corrected the import statement for 'Categories'

admin.site.register(ArticleRating)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

admin.site.register(Categories, CategoryAdmin)  # Corrected the registration for 'Categories'
admin.site.register(Article)  # Registered the 'Article' model separately
