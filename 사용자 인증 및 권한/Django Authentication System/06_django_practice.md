# views.py Code
```
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# 1. 회원 가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# 2. 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

# 3. 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

# 4. 회원정보 수정
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

# 5. 회원 탈퇴
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
```

# signup (회원가입)

![signup](https://user-images.githubusercontent.com/104968672/189304236-a2ddc04a-1783-4946-b782-533433ecda5a.png)

# login (로그인)

![login](https://user-images.githubusercontent.com/104968672/189304800-1a4bca96-f673-4c72-9d83-59bf224219b8.png)

![login1](https://user-images.githubusercontent.com/104968672/189305669-3e09cce4-f631-49b8-b0e5-deb1289a63ed.png)

# logout (로그아웃)

![articles](https://user-images.githubusercontent.com/104968672/189304078-02bf2b55-c68f-437d-a0ac-583f85b86dc7.png)

# update (회원정보 수정)

![update](https://user-images.githubusercontent.com/104968672/189305789-dd36c41c-9867-44c8-b6eb-940bed6372e1.png)

# delete (회원탈퇴)

![delete](https://user-images.githubusercontent.com/104968672/189306116-89d4357c-fe70-43ed-80db-f1092f837df2.png)