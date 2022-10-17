# Response
- 다양한 방법으로 JSON 데이터 응답해보기
    1. HTML 응답
    2. JsonResponse()를 사용한 JSON 응답
    3. Django Serializer를 사용한 JSON 응답
    4. Django REST framework를 사용한 JSON 응답

### 1. HTML 응답
- 문서(HTML) 한 장을 응답하는 서버 확인하기
- 지금까지 Django로 응답 해오던 방식

![1](https://user-images.githubusercontent.com/104968672/196199527-5851ff12-7dc9-4bc6-9848-77bae2516ada.png)

![2](https://user-images.githubusercontent.com/104968672/196199710-9197fc7a-8866-4e85-b13a-72a8dc7c2067.png)

### 2. JsonResponse()를 사용한 JSON 응답
- 이제는 문서(HTML) 한 장을 응답하는 것이 아닌 JSON 데이터를 응답해보기
- Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능

```
# articles / views.py

from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,

            }
        )
    return JsonResponse(articles_json, safe=False)
        - articles_json 즉, 앞에 인자가 딕셔너리가 아니면 safe=False를 붙여줘야 함
```
```
# articles / ulrs.py

path('json-1/', views.article_json_1)

url로 확인해보기
```

### 3. Django Serializer를 사용한 JSON 응답
- Django의 내장 HttpResponse()를 활용한 JSON 응답
- 이전에는 JSON의 모든 필드를 하나부터 열까지 작성해야 했지만 이제는 그렇지 않음

```
# articles / views.py

from django.http.response import JsonResponse, HttpResponse

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```
```
# articles / ulrs.py

path('json-2/', views.article_json_2),

url로 확인해보기
```

**Serialization**
- "직렬화"

- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    - 즉, 어떤한 언어나 환경에서도 **"나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"**

- 변환 포맷은 대표적으로 json, xml, yaml이 있으며 **json**이 가장 보편적으로 쓰임

- 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

**Serializers in Django**
Django의 serialize()는 Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 줌

![serialize](https://user-images.githubusercontent.com/104968672/196207602-12eb5dc3-674d-455e-97ea-35f668ac3314.png)

### 4. Django REST framework를 사용한 JSON 응답
- Django REST framework (DRF)
    - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
    - Web API 구축을 위한 강력한 toolkit을 제공
    - REST framework를 작성하기 위한 여러 기능을 제공
    - DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동
    - https://www.django-rest-framework.org/

![1](https://user-images.githubusercontent.com/104968672/196206775-9caf0ee2-ea4f-40f2-a550-e3913ca5e1fa.png)

![2](https://user-images.githubusercontent.com/104968672/196206838-14449065-4f7b-4b87-9d09-de5d3288a664.png)

```
# 실질적인 Serializers 과정을 진행함

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

![3](https://user-images.githubusercontent.com/104968672/196206890-ca6959e4-e6aa-45d1-8be3-30912d1701ff.png)

```
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
        # 이 과정이 serialize(), 톱니바퀴 과정
    return Response(serializer.data)
        # Serializing된 결과에서 .data만 하면 JSON이 나온다.
```
```
# articles / ulrs.py

path('json-3/', views.article_json_3),

url로 확인해보기
```
```
# requests 라이브러리 설치

pip install requests
```
```
# gogo.py 확인

# gogo.py

import requests
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
result = response.json()

# pprint(result)
# pprint(result[0])
pprint(result[0].get('title'))
```

## 정리
- DRF를 활용하여 JSON 데이터를 응답하는 Django 서버를 구축할 것

# Djnago REST framwork - Single Model
- 단일 모델의 data를 Serialization하여 JSON으로 변환하는 방법에 대한 학습

```
# 사전 준비

python -m venv venv

interpreter 설정

pip install -r requirements.txt

Article 모델 주석 해제

python manage.py migrate

python manage.py loaddata articles.json
    - 준비된 fixtures 데이터 load
pip install djangorestframework
    - DRF 설치, 등록 및 패키지 목록 업데이트

# settings.py의 INSTALLED_APPS에 'rest_framework', 작성

pip freeze > requirements.txt
```

# ModelSerializer
- articles.serializers.py 생성
    - serializers.py의 위치나 파일명은 자유롭게 작성 가능

- ModelSerializer 작성
```
articles에 serializers.py 생성

from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
```
- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
    1. Model 정보에 맞춰 자동으로 필드를 생성
    2. serializer에 대한 유효성 검사기를 자동으로 생성
    3. .create() 및 .update()의 간단한 기본 구현이 포함됨

![1](https://user-images.githubusercontent.com/104968672/196218079-41bdfdce-d3b9-4d89-89a4-d5e6593899c0.png)

![2](https://user-images.githubusercontent.com/104968672/196218111-78a531cd-0e98-4fdc-925f-de37e1c32a95.png)

![3](https://user-images.githubusercontent.com/104968672/196218137-ebfdb926-bbe8-4674-989b-d86920bd0c44.png)

![4](https://user-images.githubusercontent.com/104968672/196218175-6d211d14-ef2e-4088-b352-9d2a95b19612.png)

![5](https://user-images.githubusercontent.com/104968672/196218216-1d1930a7-8fb5-46d5-b78d-0f3caa8b4fdb.png)

- Boojk.objects.all()이 QuerySet이다. 단일 객체 인스턴스 대신에 QuerySet 또는 객체 목록을 serialize 하려면 many=True를 작성해야 데이터를 추출할 수 있다.

# Build RESTful API - Article

![1](https://user-images.githubusercontent.com/104968672/196219345-217305e1-784d-443e-ae1a-8fe5eb86a049.png)

### GET - List
- 게시글 데이터 목록 조회하기
- DRF에서 api_view 데코레이터 작성은 필수
```
# articles / urls.py

urlpatterns = [
    path('articles/', views.article_list),
]
```
```
# articles / views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
                    # articles가 단일 객체가 아니므로 many=True 필수!
        return Response(serializer.data)
```
```
http://127.0.0.1:8000/api/v1/articles/ 응답 확인
```

**'api_view' decorator**
- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

### GET - Detail
- 단일 게시글 데이터 조회하기
- 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의
```
articles / serializers.py

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
    model = Article
    fields = '__all__'
```
```
# articles / urls.py

urlpatterns = [
    path('articles/<int:article_pk>', views.article_detail),
]
```
```
@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```
```
GET http://127.0.0.1:8000/api/v1/articles/1 응답 확인
```

### POST
- 게시글 데이터 생성하기
- 요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패 했을 경우는 400 Bad request를 응답
```
# articles / views.py

from rest_framework import status

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 성공했을 경우
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 실패했을 경우
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
```
POST http://127.0.0.1:8000/api/v1/articles/ 응답 확인

새로 생성된 데이터 확인 해보기
```

### Raising an exception on invalid data
- "유효하지 않은 데이터에 대해 예외 발생시키기"
- is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환
```
view 함수 코드 변경
# articles / views.py

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=Ture):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

### DELETE
- 게시글 데이터 삭제하기
- 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답 (명령을 수행했고 더 이상 제공할 정보가 없는 경우)
```
# articles / views.py

@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
```
DELETE http://127.0.0.1:8000/api/v1/articles/21/ 응답 확인
```

### PUT
- 게시글 데이터 수정하기
- 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태 코드 응답
```
# articles/views.py

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        # serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```
```
PUT http://127.0.0.1:8000/api/v1/articles/1/ 응답 확인

수정된 데이터 확인 해보기
```

# Django REST framework - N : 1 Relation
- N : 1 관계에서의 모델 data를 Serialization하여 JSON으로 변환하는 방법 학습
```
# 사전 준비

articles / models.py의 Comment 모델 주석 해제 및 데이터베이스 초기화

python manage.py makemigrations

python manage.py migrate
    - Migration 진행

python manage.py loaddata articles.json comments.json
    - 준비된 fixtures 데이터 load
```

### GET - List
- 댓글 데이터 목록 조회하기
- Article List와 비교하며 작성해보기
```
# articles / serializers.py

from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
    model = Comment
    fields = '__all__'
```
```
# articles / urls.py

urlpatterns = [
    path('comments/', views.comment_list),
]
```
```
# articles / views.py

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
```
```
GET http://127.0.0.1:8000/api/v1/comments/ 응답 확인
```

### GET - Detail
- 단일 댓글 데이터 조회하기
- Article과 달리 같은 serializer 사용하기
```
# articles / urls.py
urlpatterns = [
    path('comments/<int:comment_pk>/', views.comment_detail),
]
```
```
# articles. views.py

@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
```
```
GET http://127.0.0.1:8000/api/v1/comments/1/ 응답 확인
```

### POST
- 단일 댓글 데이터 생성하기
```
# articles / urls.py

urlpatterns = [
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```
```
# articles / views.py

@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
            # commit=False가 아님 (아래 참고)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

### [참고]Passing Additional attributes to .save()
- **save()** 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
- **CommentSerializer**를 통해 Serialize되는 과정에서 Parameter로 넘어온 **article_pk**에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

```
POST http://127.0.0.1:8000/api/v1/comments/1/comments 응답 확인

에러 이유
    CommentSerializer에서 article field 데이터 또한 사용자로부터 입력 받오록 설정되어 있기 때문 (아래 참고)
```

### [참고] 읽기 전용 필드 설정
- **read_only_fields**를 사용해 외래 키 필드를 **'읽기 전용 필드'**로 설정
- 읽기 전용 필드는 데이터를 전송하는 시점에 **'해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력**하도록 함
```
# articles / serializers.py

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('article',)
```
```
POST http://127.0.0.1:8000/api/v1/comments/1/comments 응답 재확인
```

### DELETE & PUT
- 댓글 데이터 삭제 및 수정 구현하기
```
# articles / views.py

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```
```
DELETE http://127.0.0.1:8000/api/v1/comments/21/ 응답 확인
```
```
PUT http://127.0.0.1:8000/api/v1/comments/1/ 응답 확인
```

# N : 1 - 역참조 데이터 조회
1. 특정 게시글에 작성된 댓글 목록 출력하기
    - 기존 필드 override

2. 특성 게시글에 작성된 댓글의 개수 출력하기
    - 새로운 필드 추가

### 1. 특정 게시글에 작성된 댓글 목록 출력하기
- 기존 필드 override - Article Detail
    - "게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력하기"
    - Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

1. PrimaryKeyRelatedField()
```
# articles / serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        # comment_set이 N이기 때문에 N을 참조하니 many=True가 필요
    class Meta:
        model = Article
        fields = '__all__'

```

- models.py에서 **related_name**을 통해 이름 변경 가능
- 역참조 시 생성되는 **comment_set**을 override 할 수 있음
```
articles / models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- 작성 후 삭제

2. Nested relationshops (게시글 조회 했을때 pk만 아니라 댓글의 세부정보까지 주려면)
```
articles / serializers.py

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
            # 기존에 원래 있던 Field는 이렇게 작성할 수 있음

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```

- 모델 관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음
- 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현 할 수 있음
- 두 클래스의 상/하 위치를 변경해야 함

### 2. 특정 게시글에 작성된 댓글의 개수 출력하기ㅏ
- 새로운 필드 추가 - Article Detail
    - "게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력하기"
```
# articles / serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
             # source (아래 참고)

    class Meta:
        model = Article
        fields = '__all__'
             # override 되거나 추가된 Field는 여기에 read_only_fields 적용이 안됨 따라서 위쪽에 별도로 사용해야 함 (주의사항)
```

**soruce**
    - serializers field's argument
    - 필드를 채우는 데 사용할 속성의 이름
    - 점 표기법(dotted notation)을 사용하여 속성을 탐색 할 수 있음

### [주의] 읽기 전용 필드 지정 이슈
- 특정 필드를 override 혹은 추가적인 경우 **read_only_fields**가 동작하지 않으니 주의
```
# [주의사항] 사용 불가능

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    comment_count = serializers.IntegerField(source='comment_set.count')

    class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ('comment_ser', 'comment_count')


- read_only_fields를 Meta에 쓸 수 있는 경우는 기존에 물리적으로 존재하는 Field만 가능하고 그게 아니면 반드시 위에다가 작성해야 함
```

# Django shortcuts functions
- django.shortcuts 패키지는 개발에 도움 될 수 있는 여러 함수와 클래스를 제공
- 제공되는 shortcut 목록
    - render(), redirect(), **get_object_or_404()**, **get_list_or_404()**
    - https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/

###  get_object_or_404()
- 모델 manager objects에서 **get()**을 호출하지만, 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 함
```
# articles / views.py

from django.shortcuts import get_object_or_404

article = Article.object.get(pk=article_pk)
comment = Comment.object.get(pk=comment_pk)

# 위 코드를 모두 다음과 같이 변경
article = get_object_or_404(Article, pk=article_pk)
comment = get_object_or_404(Comment, pk=comment_pk)
```
```
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk) 
```

###  get_list_or_404()
- 모델 manager objects에서 **filter()**의 결과를 반환하고 해당 객체 목록이 없을 땐 Http404를 raise 함
```
# articles / views.py

from django.shortcuts import get_object_or_404, get_list_or_404

articles = Article.object.all()
comments = Comment.object.all()

# 위 코드를 모두 다음과 같이 변경
articles = get_list_or_404(Article)
comments = get_list_or_404(Comment)
```
```
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
```

### 적용 전/후 비교
- 존재하지 않는 게시글 조회 시 이전에는 500 상태코드를 응답했지만 현재는 404 상태코드를 응답
- 어떠한 상황에서도 정확한 상태 코드를 주는 것이 API가 갖춰야 할 가장 기본적인 구조이다.
- 갖추지 않으면 소통하기가 어려워지기 때문에


### 왜 사용해야 할까?
- 클라이언트 입장에서 "서버에 오류가 발생하여 요청을 수행할 수 없다(500)"라는 원인이 정확하지 않은 에러를 마주하기 보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소

# 마무리 INDEX
- REST API

- Response JSON

- Django REST framework - Single Model

- Django REST framework - N:1 Relation
  (역참조를 JSON에서 어떻게 만들어내서 사용자에게 줄 수 있는 지 공부 필요!)