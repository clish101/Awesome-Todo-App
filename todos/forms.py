from django import forms
from .models import Todo


class NewTodoForm(forms.Form):
    text = forms.CharField(max_length=200,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control border rounded-left',
                                      'placeholder': 'Add To Schedule'}
                           ))
