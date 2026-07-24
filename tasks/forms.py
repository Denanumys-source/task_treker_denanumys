from django import forms

from .models import Task, Comment,User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description","pole", "status", "priority", "due_date", "file"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            "pole": forms.Textarea(attrs={'class': 'form-control'}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            "priority": forms.Select(attrs={'class': 'form-control'}),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "file": forms.FileInput(
                
            ),
        }


class TaskFilterForm(forms.Form):
    priority = forms.ChoiceField(
        choices=[('', 'Усі')] + Task.PRIORITY_CHOICES,
        required=False,
        label='Пріоритет'
    )
    
    status = forms.ChoiceField(
        choices=[('', 'Усі')] + Task.STATUS_CHOICES,
        required=False,
        label='Статус'
    )
    due_date = forms.DateField(
        required=False,
        label='Дата виконання',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    creator  = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label='Користувачі'
    )
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
'''
    priority = forms.ChoiceField(
            choices=[('', 'Усі')] + Task.PRIORITY_CHOICES,
            required=False,
            label='Пріоритет'
        )

    due_date = forms.DateField(
            required=False,
            label='Дата виконання',
            widget=forms.DateInput(attrs={'type': 'date'})
        )
    status = forms.ChoiceField(
            choices=[('', 'Усі')] + Task.STATUS_CHOICES,
            required=False,
            label='Статус'
        )
'''

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content","file"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Напишіть коментар..."}),
        }
