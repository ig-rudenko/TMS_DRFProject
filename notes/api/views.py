from django.db.models import When, Value
from django.db.models import Case
from django.db.models.functions.text import Length, Concat, Substr, CharField
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer, CommentSerializer, TagSerializer, NoteCreateSerializer
from ..models import Note, Comment, Tag


class NoteListCreateAPIView(ListCreateAPIView):
    serializer_class = NoteCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    queryset = Note.objects.all()

    # def get_queryset(self):
    #     qs = Note.objects.all().annotate(
    #         content_length=Length('content'),
    #         short_content=Case(
    #             When(content_length__gt=20, then=Concat(Substr('content', 1, 20), Value('...'))),
    #             default="content",
    #             output_field=CharField()
    #         )
    #     ).only("id", "title", "owner", "created_at", "updated_at")
    #
    #     print(qs.query)
    #     return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_url_kwarg = "note_id"
    lookup_field = "id"


class CommentListCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = "comment_id"
    lookup_field = "id"
