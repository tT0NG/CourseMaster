from django.contrib import admin
from .models import Course, ClassLog, RunningCount


class CourseAdmin(admin.ModelAdmin):
    list_display = ('class_number', 'class_title', 'class_code', 'is_active')
    list_filter = ('class_title', 'is_active')
    search_fields = ('class_number',)
    ordering = ('class_title',)
    filter_horizontal = ()



admin.site.register(Course, CourseAdmin)
admin.site.register(ClassLog)
admin.site.register(RunningCount)
