from django.contrib import admin
from django.contrib.admin import TabularInline
from django.utils.safestring import mark_safe

from .models import (Cart, Favorite, Follow, Ingredient, IngredientAmount,
                     Recipe, Tag)


class IngredientInline(TabularInline):
    model = IngredientAmount
    extra = 2


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'author', 'get_image',
    )
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name', 'author')
    ordering = ('author',)
    empty_value_display = '-'
    inlines = (IngredientInline,)

    def count_favorites(self, obj):
        count = obj.favorites.count()
        if count:
            return count
        return None

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" hieght="30"')

    get_image.short_description = 'Изображение'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__username',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user__username',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')
