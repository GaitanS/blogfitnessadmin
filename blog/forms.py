from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    Formular pentru adăugarea comentariilor.
    """
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele tău'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email-ul tău'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentariul tău', 'rows': 4}),
        }
        labels = {
            'name': 'Nume',
            'email': 'Email',
            'content': 'Comentariu',
        }
