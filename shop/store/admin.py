from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'quantity', 'price', 'created_at', 'size', 'metal_product', 'get_photo')
    list_editable = ('price', 'quantity', 'size', 'metal_product')
    list_display_links = ('title',)
    list_filter = ('title', 'price')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GalleryInline]

    # Adminkada rasm korinishi uchun javobgar !
    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')
            except:
                return 'NO PHOTO'
        else:
            return 'NO PHOTO'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gallery)
