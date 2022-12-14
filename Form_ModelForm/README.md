# Django Form
### 개요
- 지금까지 HTML form, Input tag를 통해서 사용자로부터 데이터를 받았음
- 현재 우리 Django 서버는 들어오는 요청을 모두 수용하고 있는데, 이러한 요청 중에는 비정상적인 혹은 악의적인 요청이 있다는 것을 생각해야 함
- 이처럼 사용자가 입력한 데이터가 우리가 원하는 데이터 형식이 맞는지에 대한 **유효성검증**이 반드시 필요
    - 이러한 유효성 검증은 많은 부가적인 것들을 고려해서 구현해야 하는데, 이는 개발 생산성을 늦출뿐더러 쉽지 않은 작업임
- **Django Form**은 이 과정에서 과중한 작업과 반복 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만들어 줌

### From에 대한 Django의 역할
- From은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
- Django는 Form과 관련된 유효성 검사를 **단순화하고 자동화** 할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있다.
- 개발자가 필요한 핵심 부분만 집중할 수 있도록 돕는 프레임워크의 특성

### Django는 Form에 관련된 작업의 세 부분을 처리
1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

# The Django Form Class
### 개요
- Form Class
    - Django form 관리 시스템의 핵심

### Form Class 선언
- Form Class를 선언하는 것은 Model Class를 선언하는 것과 비슷하다. 비슷한 이름의 필드 타입을 많이 가지고 있다. (다만 이름만 같을 뿐 같은 필드는 아님)
- Model과 마찬가지로 상속을 통해 선언(forms 라이브러리의 Form 클래스를 상속 받음)

- 앱 폴더에 forms.py를 생성 후 ArticleForm Class 선언

![11](https://user-images.githubusercontent.com/104968672/188520987-9ae7183c-be2a-43d9-8aff-a0867ff5bfb4.png)

- form에는 model field와 달리 TextField가 존재하지 않음
- 모델의 TextField처럼 사용하려면 어떻게 작성할 수 있을 지 곧 뒷 내용에서 확인

![22](https://user-images.githubusercontent.com/104968672/188521008-c791a451-3f56-4106-a965-2ccf2755b4fe.png)

* "Form Class를 forms.py에 작성하는 것은 규약이 아니다."
* 파일 이름이 달라도 되고 models.py나 다른 어디에도 작성 가능, 다만 더 나은 유지보수의 관점 그리고 관행적으로 forms.py 파일 안에 작성하는 것을 권장

### 'new' view 함수 업데이트

![33](https://user-images.githubusercontent.com/104968672/188521027-95191ce0-a9f0-4452-984b-23d8322c7049.png)

### 'new' 템플릿 업데이트

![44](https://user-images.githubusercontent.com/104968672/188521042-b9510b62-d552-478e-be4d-9fba108c8682.png)

### 업데이트 후 출력 확인
- view 함수에서 정의한 ArticleForm의 인스턴스(form)하나로 input과 lable 태그가 모두 렌더링 되는 것을 확인하기
- 각 태그의 속성 값들 또한 자동으로 설정 되어있음

![55](https://user-images.githubusercontent.com/104968672/188521061-dd7b5d3a-1e86-400a-b164-4dcb4e71377b.png)

### From rendering options
- <'label'> & <'input'> 쌍에 대한 3가지 출력 옵션
1. as_p()
    - 각 필드가 단락(<'p'>태그)으로 감싸져서 렌더링
2. as_ul()
    - 각 필드가 목록 항목(<'li'>태그)으로 감싸져서 렌더링
    - <'ul'>태그는 직접 작성해야 한다,
3. as_table()
    - 각 필드가 테이블(<'tr'>태그)행으로 감싸져서 렌더링
- 특별한 상황이 아니면 as_p()만 사용할 예정

### Django의 2가지 HTML input 요소 표현
1. Form fields
    - 입력에 대한 유효성 검사 로직을 처리
    - 템플릿에서 직접 사용됨
    ```
    # 예시
    forms.CharField()
    ```
2. Widgets
    - 웹 페이지의 HTML input 요소 렌더링을 담당
        - input 요소의 단순한 출력 부분을 담당
    - Widgets은 반드시 form fields에 할당됨
    ```
    # 예시
    forms.CharField(widget=forms.Textarea)
    ```

# Widgets
### 개요
- Django의 HTML input element의 표현을 담당
- 단순히 HTML 렌더링을 처리하는 것이며 유효성 검증과 아무런 관계가 없음
    - "웹 페이지에서 input element의 단순 raw한 렌더링만을 처리하는 것일 뿐"

### Textarea 위젯 적용하기

![11](https://user-images.githubusercontent.com/104968672/188521445-a49309f2-1f6c-4a8b-ad88-17dbbd2e4848.png)

- 출력 결과 확인하기
- 다양한 built-in 위젯
    - https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets

![22](https://user-images.githubusercontent.com/104968672/188521465-8ba66309-c8c9-453f-b10a-e7082f53ef6f.png)

### Form fields와 widget 응용하기

![33](https://user-images.githubusercontent.com/104968672/188521471-b7c3053f-1c76-45f1-a4a7-461ca56bf4d5.png)

- 출력 결과를 확인하고 앞으로 어떻게 조합해서 사용할 수 있는지는 form field와 widgets 공식문서를 찾아보며 사용하도록 함

![44](https://user-images.githubusercontent.com/104968672/188521480-19baa998-70ac-4ea1-b035-076417a2fd22.png)

# Django ModelForm
### 개요
- Form Class를 작성하면서 든 생각
    - "Model이랑 너무 중복되는 부분이 많은 거 같다?"
- 이미 Article Model Class에 필드에 대한 정보를 작성했는데 이를 Form에 맵핑하기 위해 Form Class에 필드를 재정의 해야만 했음
- ModelForm을 사용하면 이러한 Form을 더 쉽게 작성할 수 있음

### MoelForm Class
- Model을 통해 Form Class를 만들 수 있는 helper class
- ModelForm을 Form과 똑같은 방식으로 View 함수에서 사용

### ModelForm 선언
- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

![55](https://user-images.githubusercontent.com/104968672/188521541-6033cefc-9ba3-4344-9807-c8ba3ad861a2.png)

- 기존 ArticleForm은 주석처리

### ModelForm에서의 Meta Class
- ModelForm의 정보를 작성하는 곳
- ModelForm을 사용할 경우 참조 한 모델이 있어야 하는데, Meta class의 model 속성이 이를 구성함
    - 참조하는 모델에 정의된 field 정보를 Form에 적용함

        ![11](https://user-images.githubusercontent.com/104968672/188522209-8066f25f-aba9-46f0-a3f5-f83c67b93d21.png)

- field 속성에 '__all__'를 사용하여 모델의 모든 필드를 포함할 수 있음
- 또는 exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음

![22](https://user-images.githubusercontent.com/104968672/188522234-8a10e4d5-46f4-40ac-b606-867678a4e070.png)

### [참고] Meta data
- "데이터를 표현하기 위한 데이터"
- 예시 : '사진 파일'
    - 사진 데이터
    - 사진 데이터의 데이터(촬영 시각, 렌즈, 조리개 값 등)
    - 사진 데이터에 대한 데이터(== 사진의 Meta data)

### [참고] 참조 값과 반환 값
- 호출하지 않고 이름만 작성하는 이 방식은 어떤 의미일까?

![33](https://user-images.githubusercontent.com/104968672/188522244-ba19f701-c6c0-4cca-bd12-4b2e1724f29d.png)

- 함수를 예시로 들면 아래와 같은 함수가 있을 때 함수의 이름을 그대로 출력하는 것과 호출 후의 결과를 비교

![44](https://user-images.githubusercontent.com/104968672/188522258-e39f7be6-a7bf-42da-84a0-e0e04141a8f7.png)

- 첫번째 결과는 함수의 **참조 값**을 출력
- 두번째 결과는 함수의 **반환 값**을 출력

- 언제 참조 값을 사용할까?
    - 함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 "**필요한 시점**"에 호출하는 경우

        ![55](https://user-images.githubusercontent.com/104968672/188522274-8c88892e-9a4f-4f6e-a61b-d0679c03928d.png)

    - view 함수의 참조 값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view 함수를 "필요한 시점에" 사용하기 위해서

- 결국 클래스도 마찬가지
- Article이라는 클래스를 "호출하지 않고 (== model을 인스턴스로 만들지 않고)" 작성하는 이뉴는 ArticleForm이 해당 클래스를 필요한 시점에 사용하기 위함
- 더불어 이 경우에는 인스턴스가 필요한 것이 아닌, 실제 Article 모델의 삼조 값을 통해 해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유도 있음

![66](https://user-images.githubusercontent.com/104968672/188522298-a05f8dbd-ab45-4838-9482-70809e8f2436.png)

### 주의사항
- Meta 클래스는 왜 여기에 작성할까..
    - 클래스 안에 클래스? 파이썬에서는 Inner class 혹은 Nested class라고 하는데 이건 지금 시점에서 중요한 것은 아님
        - 파이썬의 문법적 개념으로 접근하지 말 것
- 단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록 ModelForm의 설계가 이렇게 되어있을 뿐 우리는 ModelForm의 역할과 사용법을 숙지해야 함
- 우리가 상속하고 있는 부모 클래스인 ModelForm이 궁금하다면?
    - https://github.com/django/django/blob/7bdd09d016f418719f2d0297f58bd81c5349101d/django/forms/models.py#L286

# ModelForm with view functions
### 개요
- ModelForm으로 인한 view 함수의 구조 변화 알아보기

### CREATE
- 유효성 검사를 통과하면
    - 데이터 저장 후
    - 상세 페이지로 리다이렉트
    
    ![11](https://user-images.githubusercontent.com/104968672/188544722-7d0f25e1-7fef-47ad-bac1-5a434930be67.png)

- 통과하지 못하면
    - 작성 페이지로 리다이렉트

### "is_valid()" method
- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
- 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()를 제공하여 개발자의 편의를 도움

### form 인스턴스의 errors 속성
- is_valid()의 반환 값이 False인 경우 form 인스턴스의 errors 속성에 값이 작성되는데, 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨

    ![22](https://user-images.githubusercontent.com/104968672/188544780-9c2897d8-c46b-4f01-a189-d7cfa213f2a7.png)

- title에 공백을 넣고 제출해보기

    ![33](https://user-images.githubusercontent.com/104968672/188544816-5242a2f3-db6a-4bcb-8e81-a9df848dbcdc.png)

- 이와 같은 특징을 통해 다음과 같은 구조로 코드를 작성하면 유효성 검증을 실패했을 때 사용자에게 실패 결과 메세지를 출력해줄 수 있음

    ![44](https://user-images.githubusercontent.com/104968672/188544843-7ca2e3ea-417f-4a2c-bbcf-6c5a72304254.png)

### The "save()" method
- form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정함
    - 제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(CREATE)
    - 제공되면 save()는 해당 인스턴스를 수정(UPDATE)

        ![55](https://user-images.githubusercontent.com/104968672/188544879-0aa4513d-ae7b-4efa-bd3a-d437e413c26d.png)

### UPDATE
- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
1. request.POST
    - 사용자가 form을 통해 전송한 데이터(새로운 데이터)
2. instance
    - 수정이 되는 대상

- edit - view 수정

    ![66](https://user-images.githubusercontent.com/104968672/188544918-94c8382d-6e96-4be5-87da-5752ed5a070d.png)

- edit - template 수정

    ![77](https://user-images.githubusercontent.com/104968672/188544948-53f90305-57b2-4f8b-8893-d78411cde53e.png)

- update - view 수정

    ![88](https://user-images.githubusercontent.com/104968672/188544956-f87cd2a8-afad-4383-9110-968f9f79c9f2.png)

### [참고] ModelForm 키워드 인자 data와 instance 살펴보기
- https://github.com/django/django/blob/7bdd09d016f418719f2d0297f58bd81c534910d/django/forms/models.py#L286

![99](https://user-images.githubusercontent.com/104968672/188545008-10792911-ca6f-4b4b-b97f-7da3a40c6a5c.png)

### Form과 ModelForm
- ModelForm이 Form보다 더 좋은 것이 아니라 각자 역할이 다른 것
- Form
    - 사용자로부터 받은 데이터가 DB와 연관되어 있지 않는 경우에 사용
    - DB에 영향을 미치지 않고 단순 데이터만 사용되는 경우
    -(예시 - 로그인, 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음)
- ModelForm
    - 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우에만 사용
    - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할 지 이미 않고 있기 때문에 곧바로 save() 호출이 가능

# Widgets 활용하기
### 위젯을 작성하는 2가지 방법

![11](https://user-images.githubusercontent.com/104968672/188545407-200253c1-c2c6-4431-959d-8cc0bbe57063.png)

### Widgets 활용하기

![22](https://user-images.githubusercontent.com/104968672/188545421-244e4b69-b56b-4ad6-afff-5eb843b340d4.png)

# Handling HTTP requests
### 개요
- "HTTP requests 처리에 따른 view 함수 구조 변화"
- new-create, edit-update의 view 함수 역할 잘 살펴보면 하나의 공통점과 하나의 차이점이 있음
- **공통점**
    - new-create는 모두 CREATE 로직을 구현하기 위한 공통 목적
    - edit-update는 모두 UPDATE 로직을 구현하기 위한 공통 목적
- **차이점**
    - new와 edit는 GET 요청에 대한 처리만을, Create와 Update는 POST 요청에 대한 처리만을 진행
- 이 공통점과 차이점을 기반으로, 하나의 view 함수에서 method에 따라 로직이 분리되도록 변경

### Create
- new와 create view 함수를 합침
- 각각의 역할을 request.method 값을 기준으로 나뉨

![11](https://user-images.githubusercontent.com/104968672/188759816-99facbc4-eb34-4ffb-b8cd-34aabf5290de.png)

- 이제는 불필요해진 new의 view 함수와 url path를 삭제

![22](https://user-images.githubusercontent.com/104968672/188759848-0d71eb7f-d6c2-4e1a-879c-01fd13caf499.png)

- new.html -> create.html 이름 변경 및 action 속성 값 수정

![33](https://user-images.githubusercontent.com/104968672/188759870-804de7fc-3a52-4cfb-a760-266801383707.png)

- new.html -> create.html 이름 변경으로 인한 템플릿 경로 수정

![44](https://user-images.githubusercontent.com/104968672/188759889-4c401950-d94e-4721-b654-dd004ab75ec5.png)

- index 페이지에 있던 new 관련 링크 수정

![55](https://user-images.githubusercontent.com/104968672/188759907-479e293a-5966-436e-b6db-09fe452e90c3.png)

### context의 들여쓰기 위치
- 이렇게 작성하면 if form.is_valid():에서 false로 평가 받았을 때 이어질 코드가 없음

![66](https://user-images.githubusercontent.com/104968672/188759923-3dc42ae6-a5d4-420c-8c65-d2938ad2da27.png)

- 반면 아래와 같이 작성하면 if form.is_valid():에서 false로 평가 받았을 때 에러 정보가 담긴 form 인스턴스가 context로 넘어갈 수 있음

![77](https://user-images.githubusercontent.com/104968672/188759937-bd8b9a42-d2a1-430f-ac01-90861fa4d779.png)

