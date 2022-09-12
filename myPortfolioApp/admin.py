from django.contrib import admin
from myPortfolioApp.models import Portfolio

# Register your models here.
class PorfolioAdmin(admin.ModelAdmin):
    list_display = ('title','publish','is_available','is_public')
    list_filter = ('publish','is_available')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Portfolio,PorfolioAdmin)
