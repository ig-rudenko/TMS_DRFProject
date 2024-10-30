from django.db.models import When, Value
from django.db.models import Case
from django.db.models.functions.text import Length, Concat, Substr, CharField
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage

from .filters import NoteFilter
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    NoteSerializer,
    CommentSerializer,
    TagSerializer,
    NoteCreateSerializer,
    NoteShortSerializer,
    ImageUploadSerializer,
)
from ..models import Note, Comment, Tag


class NoteListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filterset_class = NoteFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return NoteCreateSerializer
        return NoteShortSerializer

    def get_queryset(self):
        qs = (
            Note.objects.all()
            .select_related("owner")  # ForeignKey
            .prefetch_related("tags")  # ManyToMany
            .annotate(
                content_length=Length("content"),
                short_content=Case(
                    When(
                        content_length__gt=200,
                        then=Concat(Substr("content", 1, 200), Value("...")),
                    ),
                    default="content",
                    output_field=CharField(),
                ),
            )
            .only("id", "title", "owner", "created_at", "updated_at", "owner__username")
        )

        # params = self.request.query_params
        #
        # if params.get("search"):
        #     # Либо поиск по заголовку, либо по тексту
        #     qs = qs.filter(
        #         Q(title__icontains=params["search"])
        #         | Q(content__icontains=params["search"]),
        #     )
        #
        # if params.get("owner"):
        #     # Поиск по автору
        #     qs = qs.filter(owner__username=params["owner"])
        #
        # if params.get("from"):
        #     qs = qs.filter(created_at__gte=params["from"])
        #
        # if params.get("to"):
        #     qs = qs.filter(created_at__lte=params["to"])
        return qs

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


class TagListAPIView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None
