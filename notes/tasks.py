import random
import time

from django.apps import apps
from celery import shared_task


@shared_task()
def note_checker(note_id: int):
    Note = apps.get_model('notes.Note')

    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return "Запись не найдена"

    if note.status != Note.Status.waiting.value:
        return "Запись уже проверена"

    print('Проверка новой публикации...')
    note.status = Note.Status.analyzing.value
    note.save()

    # Логика анализа новой публикации.
    time.sleep(10)  # Задержка
    # ================================

    if random.random() > 0.5:
        note.status = Note.Status.published.value
    else:
        note.status = Note.Status.cancelled.value
    note.save()

    return f"Публикация '{note.id}' была '{note.status}'"
