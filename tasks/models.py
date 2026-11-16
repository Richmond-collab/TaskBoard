from django.db import models

# Create your models here.

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    tags = models.ManyToManyField(Tag, blank=True)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='MEDIUM'
    )

    due_date = models.DateField(null=True, blank=True)

    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.task.title}"
