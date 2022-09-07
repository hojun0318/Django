# 로그인

## 대체하기 1단계 (대체 User 만들기)
### # accounts -> models.py
```
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
```

## 대체하기 2단계
### project -> settingd
```
# 프로젝트 중간에 하면 안됨
AUTH_USER_MODEL = 'accounts.User'
```

# 대체하기 3단계
### # accounts -> admin.py
```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
```

# 로그인 구현
### accounts -> urls.py
```
path('login/', views.login, name='login'),
```

### accounts -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

### accounts -> templates -> accounts -> login.html
```
{% extends 'base.html' %}
{% comment %} 이게 바로 AuthenticationForm이다. {% endcomment %}
{% block content %}
    <h1>LOGIN</h1>
    <form action="{% url 'accounts:login' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

### templates -> base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">
    <h3>{{ user }}</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

# 로그아웃
### acount -> urls.py
```
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
```

### account -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
```

### templates -> base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">
    <h3>{{ user }}</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

# 회원가입 (UserCreationForm)
### accounts -> urls.py
```
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
```

### accounts -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
        pass
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

### accounts -> templates -> accounts -> signup.html
```
{% extends 'base.html' %}

{% block content %}
    <h1>SIGNUP</h1>
    <form action="{% url 'accounts:signup' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

### settings.py (한국어 설정)
```
"""
Django settings for crud project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y1hz6+-p3*6r^1so9_5(v2jsirveqclpyk5g!3+cp)k(g=jk)*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'articles',
    'accounts',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'
```

### templates -> base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">
    <h3>{{ user }}</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <a href="{% url 'accounts:signup' %}">Signup</a>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

### accounts -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

### accounts -> forms.py(생성)
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
    # 현재 디렉토리의 models.py에 있음
        # model = User
    # Django는 User를 참조할때 직접 참조하는 것을 권장하지 않음!
    # get_user_model이라는 함수로 간접적으로 호출 (권장사항)
        model = get_user_model()
```

### accounts -> views.py
```
# CustomUserCreationForm으로 변경시켜 줌
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

# 회원정보 수정
### accounts -> forms.py
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
    # 현재 디렉토리의 models.py에 있음
        # model = User
    # Django는 User를 참조할때 직접 참조하는 것을 권장하지 않음!
    # get_user_model이라는 함수로 간접적으로 호출 (권장사항)
        model = get_user_model()
```

# 회원정보 수정
### account -> views.py
```
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

# 회원정보 수정
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
```

### accounts -> forms.py
```
# 이메일은 옵션이라 입력하지 않아도 가입 가능
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
```

### accounts -> views.py
```
# 회원가입 후 곧바로 로그인을 해야 한다면
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
```

# 회원 탈퇴
### accounts -> urls.py
```
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
]
```

### accounts -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
    return redirect('articles:index')
```

### templates -> base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">
    <h3>{{ user }}</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <a href="{% url 'accounts:signup' %}">Signup</a>
    <form action="{% url 'accounts:delete' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

### accounts -> views.py
```
# 회원탈퇴해도 세션은 남아 있음
# 탈퇴(1) 후 로그아웃(2)의 순서가 바뀌면 안됨
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
```

# 회원정보 수정 (UserChangeForm)
### accounts -> urls.py
```
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]
```

### accounts -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
        pass
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)
```

### accounts -> templates -> accounts -> update.html
```
{% extends 'base.html' %}

{% block content %}
    <h1>회원정보수정</h1>
    <form action="{% url 'accounts:update' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

```
# accounts -> forms.py
# 관리자 권한까지 설정 가능
# 즉 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정 가능해짐 즉, 수정 필요!!!!!!!
# fiels를 통해 보여주는 거 선택하는게 빠름
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
```

### accounts -> views.py
```
# 회원정보 수정하고 나서 메인 페이지로 이동
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm    # login을 위한 built-in form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
```

### templates -> base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">
    <h3>{{ user }}</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <a href="{% url 'accounts:signup' %}">Signup</a>
    <form action="{% url 'accounts:delete' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
    <a href="{% url 'accounts:update' %}">회원정보수정</a>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

# 비밀번호 변경 (PasswordChangeForm)
### accounts -> urls.py
```
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password')
]
```

### accounts -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm    # login을 위한 built-in form
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
        pass
    else:
        # 필수 1개 인자가 필요!! (request.user)
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password', context)

```

### accounts -> templates -> accounts -> change_password.html
```
{% extends 'base.html' %}

{% block content %}
    <h1>비밀번호변경</h1>
    <form action="{% url 'accounts:change_password' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

### accounts -> views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm    # login을 위한 built-in form
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
            return redirect('articles:index')
    else:
        # 필수 1개 인자가 필요!! (request.user)
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

```

### accounts -> views.py
```
# 암호 변경 시 세션 무효화 방지하기
# update_session_auth_hash()
# 암호가 변경돼도 로그아웃 되지 않도록 세션 업데이트
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm    # login을 위한 built-in form
from django.contrib.auth import update_session_auth_hash                        # 암호 변경시 세션 업데이트
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    # 사용자 실제 로그인 시켜주는 코드
    if request.method == 'POST':
        # ModelForm이면 첫번째 인자가 데이터(request.POST)
        # Form이면 첫번째 인자가 request, 두번째 인자가 데이터(request.POST)
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
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
```

### templates -> base.html
```
# 로그인을 했다면 로그인과 회원가입이 사라지고,
# 로그아웃 했다면 로그아웃과 회원정보 수정이 사라져야 됨
# 다듬는 과정 필요!
# 2가지 방법
    # is_authenticated attribute
        # True와 False로 구분
    # login_required

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">  <title>Document</title>
</head>
<body>
  <div class="container">

    {% if request.user.is_authenticated %}
      <h3>{{ user }}</h3>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
      </form>
      <a href="{% url 'accounts:update' %}">회원정보수정</a>

    {% else %}
      <a href="{% url 'accounts:login' %}">Login</a>
      <a href="{% url 'accounts:signup' %}">Signup</a>
    {% endif %}
    <hr>
    
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```

### accounts -> views.py
```
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
            return redirect('articles:index')
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

```

### articles -> templates -> articels -> index.html
```
# 인증된 상태에서만 Articles 작성하게 하기
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

### articles -> views.py
```
# 로그인된 사람만 글을 작성하고 삭제하고 수정하게 하기
# @login_required 데코레이터!!
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

### accounts -> templates -> accounts -> login.html
```
{% extends 'base.html' %}
{% comment %} 이게 바로 AuthenticationForm이다. {% endcomment %}
{% block content %}
    <h1>LOGIN</h1>
    {% comment %} # next를 처리하려면 url을 비워놔야 됨 {% endcomment %}
    {% comment %} <form action=" " method="POST"> {% endcomment %}
    <form action="{% url 'accounts:login' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

### accounts -> views.py
```
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
```

### articles -> views.py
```
# delete에는 @login_required를 붙이면 안됨, 같이 쓸 수 없다.
# required_POST와 로직상의 문제가 발생함 (405 에러)
# 둘 중 하나 포기하고 안으로 넣어주는게 필요!
# @login_required 삭제하고 require_POST를 먼저 하고 if 문으로

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

# 마무리
- The Django authentication system
    - User 모델 대체하기
        - CustomUser 모델로 대체, 선택권 없었습니다. 앞으로 프로젝트 시작할때 대체하면서 합니다.

- HTTP Cookies
    - 상태가 있는 세션 구성
        - 상태가 있는 세션을 만들기 위해서 사용했습니다. 왜? HTTP는 상태가 없으니까! 상태가 있는 구조는 바꿀 수가 없기 때문에 상태가 있는 것처럼 동작하기 위해서는 세션이 있는 것 처럼 매번 보내주는 수 밖에 없다.

- Authentication in Web requests
    - Auth built-in form 사용하기
        - 다양한 Auth built-in form을 사용해서 로그인과 로그아웃을 구현했습니다.

- Authentication with User
    - User Object와 User CRUD
        - 회원가입, 회원탈퇴, 비밀번호 변경, 정보수정까지 구현했습니다.