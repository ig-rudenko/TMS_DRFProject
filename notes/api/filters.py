from django.db.models import Q
from django_filters import rest_framework as filters

from notes.models import Note


class CreatedAtFilter(filters.FilterSet):
    from_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    to_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")


class NoteFilter(CreatedAtFilter):
    search = filters.CharFilter(method="filter_search")
    owner = filters.CharFilter(method="filter_owner")

    class Meta:
        model = Note
        fields = ["search", "owner", "from_date", "to_date"]

    def filter_search(self, queryset, name: str, value: str):
        return queryset.filter(Q(title__icontains=value) | Q(content__icontains=value))

    def filter_owner(self, queryset, name: str, value: str):
        return queryset.filter(owner__username=value)
