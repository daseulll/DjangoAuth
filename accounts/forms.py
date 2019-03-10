from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import User


class SignupForm(UserCreationForm):
    # 유효성검사: 각 필드에 대한 validators, clean_필드명, clean 로 수행
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #super()로 부모데이터를 호출하면, self.fields에 dict형태로 부모의 필드 데이터가 모두 담김
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = '이메일 형식으로 입력해주세요.'
        self.fields['username'].label = 'E-mail'
        # _('email') _와 ()를 붙이면 국제화기능 (여러언어 지원)

    def save(self, commit=True):
        user = super().save(commit=False) #user 객체를 호출
        user.email = user.username
        if commit :  # commit인자는 본연의 modelForm에 있는 인자이므로 똑같이 구현
            user.save()
        
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        # fields ...


    # def clean_username(self):
    #     value = self.cleaned_data.get('username')
    #     if value: #값이 있다면, email인지 체크
    #         validate_email(value)
    #         # 이 자체로 유효성을 검사하여, email이 아니면 오류를 발생시킨다.
    #     return value