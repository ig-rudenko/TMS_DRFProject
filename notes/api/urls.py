from django.urls import path

from . import views


# /api/v1/

urlpatterns = [
    path("notes", views.NoteListCreateAPIView.as_view(), name="note-list-create"),
    path(
        "notes/<int:note_id>",
        views.NoteRetrieveUpdateDestroyAPIView.as_view(),
        name="note-detail",
    ),
    path(
        "comments", views.CommentListCreateAPIView.as_view(), name="comment-list-create"
    ),
    path(
        "comments/<int:comment_id>",
        views.CommentRetrieveDestroyAPIView.as_view(),
        name="comment-detail",
    ),
    path("tags", views.TagListAPIView.as_view(), name="tag-list"),
    path("upload-images", views.ImageUploadView.as_view(), name="upload-images"),
]
