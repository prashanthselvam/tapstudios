from django.contrib import admin
from .models import Project, ProjectImages

# Register your models here.

class ProjectImagesInline(admin.TabularInline):
	model = ProjectImages

class ProjectAdmin(admin.ModelAdmin):
	inlines = [ProjectImagesInline]


admin.site.register(Project, ProjectAdmin)