from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


# 회원 가입
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
    # 현재 디렉토리의 models.py에 있음
        # model = User
    # Django는 User를 참조할때 직접 참조하는 것을 권장하지 않음!
    # get_user_model이라는 함수로 간접적으로 호출 (권장사항)
        model = get_user_model()
    # DB의 accounts_user에 있는 Fields만 쓸 수 있음
    # 'first_name', 'last_name' 등등 가능
        fields = UserCreationForm.Meta.fields + ('email',)

# 회원정보 수정
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)