from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required':'제목을 입력해주세요.'
        },
        max_length=64, label='제목'
    )
    description = forms.CharField(
        error_messages={
            'required':'내용을 입력해주세요.'
        }, label='내용'
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if not (name and description ):
            self.add_error('name', '값이 없습니다.')

            
