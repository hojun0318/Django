from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    user = forms.CharField(
        label='작성자',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nickname',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Chat!',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content',
        }
    )

    class Meta:
        model = Chat
        fields = '__all__'