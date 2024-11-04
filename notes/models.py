from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from notes.tasks import note_checker

User = get_user_model()


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Status(models.Choices):
        waiting = "waiting"
        analyzing = "analyzing"
        published = "published"
        cancelled = "cancelled"

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.waiting.value
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "notes"
        ordering = ["-created_at"]


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    color = models.CharField(max_length=100, default="#000000")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"
        ordering = ["name"]


class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "comments"
        ordering = ["-created_at"]


# Вызывается в самом celery worker, не используем.
# @receiver(post_save, sender=Note)
# def post_save_note(sender, instance: Note, created: bool, **kwargs):
#     print("Была сохранена запись", sender, instance, created, kwargs)
#
#     if created:
#         # Если заметка была создана, а не обновлена.
#         task_id = note_checker.delay(instance.id)  # Отправка задачи в брокер.
#         print(task_id)
