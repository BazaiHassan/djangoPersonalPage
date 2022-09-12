from django.contrib import admin
from myGithubApp.models import GithubItem

# Register your models here.
class GithubItemAdmin(admin.ModelAdmin):
    list_display = ('repository_name','publish','is_available')
    list_filter = ('publish','is_available')
    search_fields = ('repository_name', 'description')
    prepopulated_fields = {'slug':('repository_name',)}


admin.site.register(GithubItem,GithubItemAdmin)
