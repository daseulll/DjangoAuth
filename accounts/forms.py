from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import User, Profile


class SignupForm(UserCreationForm):
    bio = forms.CharField(required=False)
    website_url = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #super()로 부모데이터를 호출하면, self.fields에 dict형태로 부모의 필드 데이터가 모두 담김
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = '이메일 형식으로 입력해주세요.'
        self.fields['username'].label = 'E-mail'

    def save(self):
        user = super().save(commit=False) #user 객체를 호출
        user.email = user.username
        user.save()

        bio = self.cleaned_data.get('bio', None)
        website_url = self.cleaned_data.get('website_url', None)
        Profile.objects.create(user=user, bio=bio, website_url=website_url)
        
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('bio', 'website_url')


    # def clean_username(self):
    #     value = self.cleaned_data.get('username')
    #     if value: #값이 있다면, email인지 체크
    #         validate_email(value)
    #         # 이 자체로 유효성을 검사하여, email이 아니면 오류를 발생시킨다.
    #     return value
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'website_url']