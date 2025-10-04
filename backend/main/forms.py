from django import forms
from django.core.validators import EmailValidator, MinLengthValidator

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=50,
        required=True,
        validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя'
        })
    )
    
    email = forms.EmailField(
        label='Email',
        required=True,
        validators=[EmailValidator()],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@mail.ru'
        })
    )
    
    message = forms.CharField(
        label='Сообщение',
        required=True,
        min_length=10,
        max_length=1000,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Введите ваше сообщение (минимум 10 символов)'
        })
    )