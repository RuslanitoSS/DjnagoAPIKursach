from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Student, Project, Event

@admin.register(Student)
class StudentAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'university', 'faculty', 'course_number')
    search_fields = ('first_name', 'last_name', 'university', 'faculty')
    list_filter = ('university', 'faculty', 'course_number')
    fieldsets = (
        ("Основная информация", {
            "fields": ('first_name', 'last_name', 'university', 'faculty', 'course_number'),
        }),
    )
    ordering = ('last_name', 'first_name')

@admin.register(Project)
class ProjectAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'field', 'student_count', 'description_short')
    search_fields = ('title', 'field')
    list_filter = ('field',)
    fieldsets = (
        ("Основная информация", {
            "fields": ('title', 'field', 'description'),
        }),
        ("Связи", {
            "fields": ('students',),
        }),
    )
    filter_horizontal = ('students',)

    @admin.display(description="Количество участников")
    def student_count(self, obj):
        return obj.students.count()

    @admin.display(description="Краткое описание")
    def description_short(self, obj):
        return obj.description[:50] if obj.description else "Нет описания"

@admin.register(Event)
class EventAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'field', 'address', 'student_count', 'description_short')
    search_fields = ('title', 'field', 'address')
    list_filter = ('field',)
    fieldsets = (
        ("Основная информация", {
            "fields": ('title', 'field', 'address', 'description'),
        }),
        ("Связи", {
            "fields": ('students',),
        }),
    )
    filter_horizontal = ('students',)

    @admin.display(description="Количество участников")
    def student_count(self, obj):
        return obj.students.count()

    @admin.display(description="Краткое описание")
    def description_short(self, obj):
        return obj.description[:50] if obj.description else "Нет описания"
