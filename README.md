# Django를 시작하기 전 지금까지 배운 것은?
- Python을 사용하고, HTML, CSS도 배워서 웹 페이지도 구성할 수 있는 상태
- 하지만 '웹 서비스 하나 만들어줄 수 있어? 라고 누가 묻는다면?

# 웹 서비스 개발에는 무엇이 필요 할까?
- 로그인, 로그아웃, 회원관리, 데이터베이스, 서버, 클라이언트, 보안 등
- 너무 많은 기술들이 필요 -> 이걸 어떻게 다 만들어야 할까?
- 모든 걸 직접 만들 필요 없음
- 잘 만들어진 것들을 가져다가 좋은 환경에서 잘 쓰기만 하면 되는 세상

# Framework 이해하기
- 전 세계의 수많은 개발자들이 이미 수없이 많이 개발해 봤고, 그 과정에서 자주 사용되는 부분들을 재사용 할 수 있게 좋은 구조의 코드로 만들어 두었음
- 그러한 코드들을 모아 놓은 것,

**즉 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것 = 프레임워크(Framework)**

- 소프트웨어 프레임워크는 복잡한 문제를 해결하거나 서술하는 데 사용되는 기본 개념 구조
- 따라서, Framework를 잘 사용하기만 하면 웹 서비스 개발에 있어서 모든 것들을 하나부터 열까지 직접 개발할 필요 없이, 내가 만들고자 하는 본질(로직)에 집중해 개발할 수 있음
- 소프트웨어의 생산성과 품질을 높임

# Django를 배워야하는 이유
- 1. Python으로 작성된 프레임 워크
    - Python이라는 언어의 강력함과 거대하 커뮤니티
- 2. 수많은 여러 유용한 기능들
- 3. 검증된 웹 프레임워크
    - 화해, Toss, 두나무, 당근마켓, 요기요 등
    - 유명한 많은 서비스들이 사용한다는 것 == 안정적으로 서비스를 할 수 있다는 검증

# WEB
### WWW(Wordl WIde Web)
- 인터넷이란 전세계에 퍼져있는 거미줄같은 연결망
    - 실제로 해저에 케이블로 전세계는 연결되어 있음
- 인터넷을 이용한다는 것은 결국 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것

# 클라이언트 - 서버 구조
- 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작
- 클라이언트와 서버 역시 하나의 컴퓨터이며 이들이 상호작용하는지에 대한 간소화된 다이어그램은 다음과 같음
    - Client --(requests)--> Server
    - Client <--(responses)-- Server

### 클라이언트
- 웹 사용자의 인터넷에 연결된 장치 (예를 들어 Wi-Fi에 연결된 컴퓨터 또는 모바일)
- CHrome 또는 Firefox와 같은 웹 브라우저
- 서비스를 요청하는 주체

### 서버
- 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
- 요청에 대해 서비스를 응답하는 주체

# Web Browser와 Web Page
### 웹 브라우저란?
- 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
- 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는(렌더링, Rendering)프로그램

### 웹 브라우저 예시
- 우리가 보고 있는 웹 페이지는 사실 HTML 문서 파일 하나
- Google 홈페이지를 예로 들면 우리는 구글 로고가 있는 예쁜 화면을 보지만, 사실 빼곡한 코드로 작성된 HTML 문서를 서버로부터 전달받게 됨
- 즉, 웹 페이지 코드를 받으면 우리가 보는 화면처럼 바꿔주는 것이 바로 웹 브라우저
- HTML / CSS / JS 등의 코드를 읽어 실제 사람이 볼 수 있는 화면으로 만들어 줌

# 웹 페이지란?
- 웹에 있는 문서
    - 우리가 보는 화면 각각 한 장 한 장이 웹 페이지
- 웹 페이지 종류
    - 1. 정적 웹 페이지
    - 2. 동적 웹 페이지

# 정적 웹 페이지
- Static Web Page
- 있는 그대로를 제공하는 것(Served as-is)을 의미
- 우리가 지금까지 작성한 웹 페이지이며 한 번 작성된 HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습을 전달되는 것
    - == 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지
    - == 같은 상황에서 모든 사용자에게 동일한 정보를 표시

# 동적 웹 페이지
- Dynamic Web Page
- 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
- 웹 페이지의 내용을 바꿔주는 주체 == '서버'
    - 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
    - 이렇게 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크가 바로 우리가 배울 'Django'
- 다양한 서버 사이드 프로그래밍 언어(Python, Java, C++ 등) 사용 가능
- 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐
- 이 중에서 Python을 이용해서 개발할 수 있는 프레임워크 Django를 학습하는 것

# Django 구조 이해하기 (MTV Design Pattern)
## Design Pattern
- 부산의 명물이라는 광안대교, 이러한 다리는 어떻게 만들까?
    - 광안대교 같은 다리를 현수교(Suspension Bridge)라고 함
    - 교량의 양쪽 끝과 가운데 솟아있는 주탑에 케이블을 두고 상판을 메다는 형식의 공법
    - 이와 똑같은 방식을 사용해서 인천대교, 이순신대교 등이 만들어졌음
    - 즉, 여러번 짓다보니 "자주 사용되는 구조가 있다는 것을 알게 되었고 이를 일반화해서 하나의 공법"으로 만들어 둔 것

- 소프트웨어에서의 관점
    - 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하며, 이를 처리하는 해결책 사이에도 공통점이 있다는 것을 발견
    - 이러한 유사점을 패턴이라 함

### 소프트웨어 디자인 패턴
- 소프트웨어도 수십년간 전 세계의 개발자들이 계속 만들다 보니 자주 사용되는 구조와 해결책이 있다는 것을 알게 됨
- 앞서 배웠던 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나
- 자주 사용되는 소프트웨어의 구조를 소수의 뛰어난 엔지니어가 마치 건축의 공법처럼 일반적인 구조화를 해둔 것

### 소프트웨어 디자인 패턴의 목적
- 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시
- 프로그래머가 어플리케이션이나 시스템을 디자인할 때 발생하는 공통된 문제들을 해결하는데 형식화 된 가장 좋은 관행

### 소프트웨어 디자인 패턴의 장정
- 디자인 패턴을 알고 있다면 서로 복잡한 커뮤니케이션이 매우 간단해짐
* Before
    - "무언가 서비스를 요청하는 쪽을 하나 만들고.. 둘 사이에 데이터를 주고 받는 방식을 정의 한 다음.. 요청을 처리하는 쪽을 하나 따로 개발해서.. 다수의 요청을 처리하는 구조로 만들어보자..!"
* After
    - "우리 이거 클라이언트-서버 구조로 구현하자"
- **다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션ㅇ늬 효율성을 높이는 기법**

# Django's Design Pattern
### Django에서의 디자인 패턴
- Django에도 이러한 디자인 패턴이 적용이 되어 있는데, Django에 적용된 디자인 패턴은 **MTV 패턴**이다.
- MTV 패턴은 **MVC 디자인 패턴**을 기반으로 조금 변형된 패턴이다.

### MVC 소프트웨어 디자인 패턴
- MVC는 Model - View - Controller의 준말
- 데이터 및 논리제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
- 하나의 큰 프로그램을 3가지 역할로 구반한 개발 방법론
    - 1. Model: 데이터와 관련된 로직을 관리
    - 2. View: 레이아웃과 화면을 처리
    - 3. Controller: 명령을 model과 view 부분으로 연결

### MVC 소프트웨어 디자인 패턴의 목적
- "관심사 분리"
- 더 나은 업무의 분리와 향상된 관리를 제공
- 각 부분을 독립적으로 개발할 수 있어, 하나를 수정하고 싶을 때 모두 건들지 않아도 됨
    - == 개발 효율성 및 유지보수가 쉬워짐
    - == 다수의 멤버로 개발하기 용이함

### Django에서의 디자인 패턴
- Django는 MVC 패턴을 기반으로 한 MTV 패턴을 사용
- 두 패턴은 서로 크게 다른 점은 없으며 일부 역할에 대해 부르는 이름이 다름
- MVC(Model - View - Controller) vs MTV(Model - Template - View)

### MTV 디자인 패턴
- Model
    - MVC 패턴에서 Model의 역할에 해당
    - 데이터와 관련된 로직을 관리
    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리

- Template
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
    - MVC 패턴에서 View의 역할에 해당

- View
    - Model & Template과 관련된 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리를 분기하는 역할
    - 동작 예시
        - 데이터가 필요하다면 model에 접근해서 데이터를 가져오고 가져온 데이터를 template로 보내 화면을 구성하고 구성된 화면을 응답으로 만들어 클라이언트에게 반환
    - MVC 패턴에서 Controller의 역할에 해당

![화면 캡처 2022-09-05 221026](https://user-images.githubusercontent.com/104968672/188457497-308bd3f5-e3be-486f-ac37-370680537649.png)

### 정리
- Django는 MTV 디자인 패턴을 가지고 있음
    - Model: 데이터 관련
    - Template: 화면 관련
    - View: Model & Template 중간 처리 및 응답 반환

# Django 기본설정
### 가상환경 설정
- 설치 전 가상환경 설정 및 활성화를 마치고 진행
```
python -m venv venv
# 가상환경을 만드는 코드(-m venv)
# 가상환경 이름이 venv
```

```
source ./venv/Scripts/activate
# 가상환경 활성화
# 생성된 venv 파일에 Scripts와 activate 파일들이 있음
```

### Package
```
# Django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치
pip install django==3.2.13
# 2021년 12월 Django 4.0 릴리즈 이후 버전을 명시하지 않으면 4.0 버전이 설치되니 주의
```
    - [참고] LTS
        - Long Term Support (장기 지원 버전)
        - 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
        - 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
        - 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함

```
# 패키지 목록 생성
pip freeze > requirements.txt
```

```
# 현재 가상환경 내 설치된 모듈 확인
pip list
```

```
# 프로젝트 생성
django-admin startproject firstpjt .
# Project 이름에는 Python이나 Django에서 사용중인 키워드 및 -(하이픈) 사용 불가
# . (dot)을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 됨
```

```
# 서버실행
python manage.py runserver
```
- 서버 실행 후 메인 페이지 확인할 것

### 프로젝트 구조

![화면 캡처 2022-09-05 222913](https://user-images.githubusercontent.com/104968672/188460877-13e98d09-a0f6-463e-b548-e05e746fb80b.png)
```
__init__.py
    # Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
    # 별도로 추가 코드를 작성하지 않음
```

```
asgi.py
    # Asynchronous Server Gateway Interface
    # Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
    # 추후 배포 시에 사용하며 지금은 수정하지 않음
```

```
settings.py
    # Django 프로젝트 설정을 관리
```

```
urls.py
    # 사이트의 url과 적절한 views의 연결을 지정
```

```
wsgi.py
    # Web Server Gateway Interface
    # Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
    # 추후 배포 시에 사용하며 지금은 수정하지 않음
```

```
manage.py
    # Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
```

### Django Application
- 애플리케이션(앱) 생성
```
python manage.py startapp articles
# 일반적으로 애플리케이션 이름은 '복수형'으로 작성하는 것을 권장
```

![화면 캡처 2022-09-05 223408](https://user-images.githubusercontent.com/104968672/188461735-18072d30-4ca6-45bf-804c-f2985406c9ea.png)

```
admin.py
    # 관리자용 페이지를 설정하는 곳
```

```
apps.py
    # 앱의 정보가 작성된 곳
    # 별도로 추가 코드를 작성하지 않음
```

```
models.py
    # 애플리케이션에서 사용하는 Model을 정의하는 곳
    # MTV 패턴의 M에 해당
```

```
tests.py
    # 프로젝트의 테스트 코드를 작성하는 곳
```

```
views.py
    # view 함수들이 정의되는 곳
    # MTV 패턴의 V에 해당
```

### 애플리케이션 등록

![화면 캡처 2022-09-05 223731](https://user-images.githubusercontent.com/104968672/188462411-b1efd850-a76a-4bfc-a017-8f6bc6d1a443.png)

- 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 반드시 추가해야 함
- INSTALLED_APPS
    - Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록

### Project & Application
- Project
    - "collection of apps"
    - 프로젝트는 앱의 집합
    - 프로젝트에는 여러 앱이 포함될 수 있음
    - 앱은 여러 프로젝트에 있을 수 있음

- Application
    - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
    - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함

### 애플리케이션 주의사항 - 1
**반드시 생성 후 등록**
- INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음

### 애플리케이션 주의사항 - 2

![화면 캡처 2022-09-05 223731](https://user-images.githubusercontent.com/104968672/188463144-751bbeef-5591-4dc9-a2fb-8c1590cebd1d.png)

- 해당 순서를 지키지 않아도 현재는 문제가 없지만, 추후 advanced 한 내용을 대비하기 위해 지키는 것을 권장

# 요청과 응답
**URL -> VIW -> TEMPLATE 순의** 작성 순서로 코드를 작성해보고 데이터의 흐름 이해하기
- 설계순서
    - 1. URL
    - 2. VEIW
    - 3. TEMPLATE

### URL

![화면 캡처 2022-09-05 223731](https://user-images.githubusercontent.com/104968672/188463956-c082dd7a-9917-4d60-93be-b002cb9b8572.png)

- path('index/', views.index)
    - index라는 경로로 들어오면 views에 있는 기능을 수행해주면 된다는 명령
    - views.index를 사용하시 위해 from articles import views 필요

### VIEW

![화면 캡처 2022-09-05 224755](https://user-images.githubusercontent.com/104968672/188464543-f5d13215-1f3e-4f7f-805b-de491ccbf4ec.png)

- Browser의 URL -> urls.py -> views.py -> index.html
    - index(request) 내의 request 파라미터에 Django가 알아서 request를 넣어서 넘겨줌
- HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
- Template에게 HTTP 응답 서식을 맡김

### render()
```
render(request, template_name, context)
```
- 주어진 template을 주어진 context data와 결합하고 rendering된 text와 함께 HttpResponse(응답) 객체를 반환하는 함수
- 1. request
    - 응답을 생성하는 데 사용되는 요청 객체
- 2. template_name
    - 템플릿의 전체 이름 또는 템플릿 이름의 경로
- 3. context
    - 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)

### Templates

![화면 캡처 2022-09-05 225255](https://user-images.githubusercontent.com/104968672/188465279-df0d0e4d-fc9a-4641-a6f2-d3b6e489e810.png)

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- Template 파일의 기본 경로
    - app 폴더 안의 templates 폴더
    - app_name/templates/
**템플릿 폴더 이름은 반드시 templates라고 지정해야 함**

### 코드 작성 순서
- 앞으로 Django에서의 코드 작성은 URL -> View -> Template 순으로 작성
**데이터의 흐름 순서**

![화면 캡처 2022-09-05 225549](https://user-images.githubusercontent.com/104968672/188465810-675fb81c-5f33-4944-b22c-78b1406bdd11.png)

### [참고] 추가 설정
- LANGUAGE_CODE
    - 모든 사용자에게 제공되는 번역을 결정
    - 이 설정이 적용 되려면 USE_I18N이 활성화(True)되어 있어야 함
    - http://www.i18nguy.com/unicode/language-identifiers.html

- TIME_ZONE
    - 데이터베이스 연결의 시간대를 나타내는 문자열 지정
    - USE_TZ가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, UTC 대신 새로 설정한 시간대의 인식 날짜 & 시간이 반환 됨
    - USE_TZ이 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의
    - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

- USE_I18N
    - Django의 번역 시스템을 활성화해야 하는 지 여부를 지정

- USE_L10N
    - 데이터의 지역화 된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
    - True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시
- USE_TZ
    - datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
    - True일 경우, Django는 내부적으로 시간대 인식 날짜 / 시간을 사용

# Django Template
**데이터 표현을 제어하는 도구이자 표현에 관련된 로직**
- Django Template을 이용한 HTML 정적 부분과 동적 컨텐츠 삽입
- Template System의 기본 목표를 숙지

- Django Template System
    - 데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당

### Django Template Language (DTL)
- Django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
    - Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 **Python 코드로 실행되는 것이 아님**
    - Django 템플릿 시스템은 단순히 Python이 HTML에 포함된 것이 아니니 주의
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심할 것

### DTL Syntax
1. Varialbe
2. Filters
3. Tags
4. Comments

### Variable
```
{{variable}}
```
- 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
    - 공백이나 구두점 문자 또한 사용할 수 없음
- dot(.)를 사용하여 변수 속성에 접근할 수 있음
- render()의 세번째 인자로{'key':value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

### Filters
```
{{variable|filter}}
```
- 표시할 변수를 수정할 때 사용
- 예시)
    - name 변수를 모두 소문자로 출력
    ```
    {{name|lower}}
    ```
- 60개의 built-in template filters를 제공
- chained가 가능하며 일부 필터는 인자를 받기도 함
```
{{name|truncatewords:30}}
```

### Tags
```
{% tag %}
```
- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요
```
{% if %}{% endif %}
```
- 약 24개의 built-in template tags를 제공

### Comments
```
{# #}
```
- Django template에서 라인의 주석을 표현하기 위해 사용
- 아래처럼 유효하지 않은 템플릿 코드가 포함될 수 있음
```
{# {% if %} text {% endif %} #}
```
- 한 줄 주석에만 사용할 수 있음 (줄 바꿈이 허용되지 않음)
- 여러 줄 주석은 {% comment %}와 {% endcomment %} 사이에 입력
```
{% comment %}
  여러 줄
  주석
{% endcommet %}
```

![11](https://user-images.githubusercontent.com/104968672/188469838-1b2bec77-e303-4f13-894b-588d19de7cb7.png)

![22](https://user-images.githubusercontent.com/104968672/188469870-0bb3f438-eda7-4259-a665-4a0f09a54e20.png)

![33](https://user-images.githubusercontent.com/104968672/188469903-e2fc48fe-8554-457c-870a-b52bc5d1023f.png)

![44](https://user-images.githubusercontent.com/104968672/188469924-e1d391b6-a772-4cea-a408-800686e4e7e4.png)

![55](https://user-images.githubusercontent.com/104968672/188469946-dd067cc0-573b-41d9-9776-04cf53865f9e.png)

### Trailing URL Slashes (참고)
- Django에서는 trailing slash 옵션이 True
    - Django는 URL 끝에 `/` 가 없다면 자동으로 붙여주는 것이 기본 설정
        - 그래서 모든 주소가 `/` 로 끝나도록 구성되어있음
        - 모든 프레임워크가 이렇게 동작하는 것은 아님
        - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 `/` 이 붙은 것과 붙지 않은 것을 다른 페이지로 보며, Django는 URL을 정규화하여 검색 엔진 로봇이 혼동하지 않도록 함
    - url을 적어줄 때 끝에 `/` 를 붙여주자
    - [https://djkeh.github.io/articles/Why-do-we-put-slash-at-the-end-of-URL-kor/](https://djkeh.github.io/articles/Why-do-we-put-slash-at-the-end-of-URL-kor/)
- 앞에 `/` 는 현재 슬래시가 시작점이라는 의미
    - `/index/` 로 anchoring하면
        - `greetings/index/` 와 같이 현재 url에서 index라는 path를 덧붙여주는 형태로 됨