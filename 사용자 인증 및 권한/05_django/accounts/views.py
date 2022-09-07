from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm    # login을 위한 built-in form
from django.contrib.auth import update_session_auth_hash                        # 암호 변경시 세션 업데이트
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            # 단축 평가 next 파라미터가 있다면 뒤는 안봄, 없다면 articles:index
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')

# create와 동일
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # save()는 user를 return
            user = form.save()
            # 회원가입 후 로그인을 해야한다면
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    # user 객체는 어디서? request 밖에 없다.
    request.user.delete()
    # 회원탈퇴 후 로그아웃 시켜야 함
    auth_logout(request)
    return redirect('articles:index')

# 회원정보 수정
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

# 패스워드 변경
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # 필수 1개 인자가 필요!! (request.user)
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)