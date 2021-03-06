from django.contrib import admin

from applications.product.models import Category, Product, Image

from applications.product.models import Category, Product, Image, Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment)
admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Image)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInAdmin
    ]


