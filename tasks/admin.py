from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Task, Category, Tag, Comment

admin.site.register(Category)
admin.site.register(Tag)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "priority",
        "due_date",
        "done"
    )

    list_filter = ("done", "priority", "category")

    search_fields = ("title", "description")

    list_editable = ("done",)

    inlines = [CommentInline]

    @admin.action(description="Mark selected tasks as done")
    def mark_done(self, request, queryset):
        updated = queryset.update(done=True)

        self.message_user(
            request,
            f"{updated} tasks marked done."
        )

    actions = ["mark_done"]
