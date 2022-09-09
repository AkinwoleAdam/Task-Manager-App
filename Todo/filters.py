import django_filters
from .models import Todo
from django_filters import CharFilter,BooleanFilter,ChoiceFilter
from django import forms
from django.forms.widgets import TextInput,Select


STATUS = (
('1','Completed'),
('0','Not Completed'),
)

class TodoFilter(django_filters.FilterSet):
  title = CharFilter(field_name='title',lookup_expr='icontains',label='Enter a KEYWORD your task title contains:')
  completed = ChoiceFilter(field_name='completed',choices=STATUS,widget=forms.Select,label="Task Status",help_text="Mark as appropriate")
  class Meta:
    model = Todo
    fields = ['title','completed']