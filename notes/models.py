from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

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
