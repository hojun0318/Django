from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
# 로그인
def login(request):
    if request.user.is_authenticated:
        return redirect('arrticles:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 처리
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

# 회원 가입
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # DB에 저장
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

# 회원 탈퇴
def delete(request):
    request.user.delete()
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
        'form': form,
    }
    return render(request, 'accounts/update.html', context)