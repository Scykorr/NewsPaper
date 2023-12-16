from django.forms import DateTimeInput
from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from .models import Post, Category


class NewsFilter(FilterSet):

    category = ModelMultipleChoiceFilter(
        field_name="postcategory__category",
        queryset=Category.objects.all(),
        label="Категория",
    )

    added_after = DateTimeFilter(
        field_name='create_date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
