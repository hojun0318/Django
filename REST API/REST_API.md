# HTTP
```
Hyper Text Transfer Protocol

HTML 문서와 같은 리소스(resource, 자원)들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)

웹에서 이루어지는 모든 데이터 교환의 기초가 됨

"클라이언트 - 서버 프로토콜" 이라고도 부름

클라이언트와 서버는 다음과 같은 개별적인 메시지 교환에 의해 통신
    - 요청(request)
        - 클라이언트에 의해 전송되는 메시지
    - 응답(response)
        - 서버에서 응답으로 전송되는 메시지
```
### HTTP 특징
```
Statelestt (무상태)
    - 동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
    - 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

- 이는 특정 페이지와 일관되게 상호작용 하려는 사용자에게 문제가 될 수 있으며, (예를 들어 e-commerce에서 장바구니를 사용하는 경우) 이를 해결하기위해 쿠키와 세션을 사용해 서버 상태를 요청과 연결하도록 함
```

### HTTP Request Methods
```
리소스에 대한 행위(수행하고자 하는 동작)를 정의

즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의

HTTP verbs 라고도 함

HTTP Method 예시
    - GET, POST, PUT, DELETE
```

### 대표 HTTP Request Methods
1. GET
    - 서버에 리소스의 표현을 요청
    - GET을 사용하는 요청은 데이터만 검색해야 함
2. POST
    - 데이터를 지정된 리소스에 제출
    - 서버의 상태를 변경
3. PUT
    - 요청한 주소의 리소스를 수정
4. DELETE
    - 지정된 리소스를 삭제

### HTTP response status codes
- 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
- 응답은 5개의 그룹으로 나뉨
    1. Informational responses (100-199)
    2. Successful responses (200-299)
    3. Redirection messages (399-399)
    4. Client error responses (400-499)
    5. Server error responses (500-599)

# Identifying resources on the WEb
```
웹에서 리소스를 식별하는 방법에 대해 학습
```

### 웹에서 리소스 식별
- HTTP 요청의 대상을 리소스(resource, 자원)라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 식별을 위해 **URI**로 식별됨

# URI
```
Uniform Resource Identifier

인터넷에서 하나의 리소스를 가리키는 문자열

가장 일반적인 URI는 웹 주소로 알려진 URL
    - 경로로 찾느냐
특정 이름공간에서 이름으로 리소스를 식별하는 URI는 URN
    - 이름으로 찾느냐
```
# [참고] URN
```
Uniform Resource Name (통합 자원 이름)

URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함 (독립적 이름)

URL의 단점을 극복하기 위해 등장했으며 자원이 어디에 위치한지 여부와 관계없이 이름만으로 자원을 식별

"하지만 이름만으로 실제 리소스를 찾는 방법은 보편화 되어있지 않아 현재는 URL을 대부분 사용"

예시
    - ISBN (국제 표준 도서 번호)
        - 국제적으로 책에 붙이는 고유 식별자
    - ISAN (국제 표준 시청각 자료번호)
        - 도서의 ISNB과 유사한 시청각 작품 및 관련 버전의 고유 식별자
```

# URL
- Uniform Resource Locator (통합 자원 위치)

- 웹에서 주어진 리소스의 주소

- 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
    - 이러한 리소스는 HTML, CSS, 이미지 등이 될 수 있음

- URL은 다음과 같이 여러 부분으로 구성되며 일부는 필수이고 나머지는 선택사항

### URL 구조
- Scheme (or protocol)
```
브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜

URL 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄

기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 mailto:, 파일을 전송하기 위핸 ftp: 등 다른 프로토콜도 존재
```

### Authority
```
Scheme 다음은 문자 패턴 ://으로 구분된 Authority(권한)이 작성됨

Authority는 domain과 port를 모두 포함하며 둘은 :(콜론)으로 구분됨

1. Domain Name
    - 요청 중인 웹 서버를 나타냄
    - 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능
    - 예를 들어 google.com의 IP 주소는 142.251.42.142

2. Port
    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
    - HTTP 프로토콜의 표준 포트는 다음과 같고 생략이 가능 (나머지는 생략 불가능)
        - HTTP - 80
        - HTTPS - 443
    - Django의 경우 8000(80+00)이 기본 포트로 설정되어 있음
```

### Path
```
웹 서버의 리소스 경로

초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화된 헝태의 구조를 표현

예를 들어 /articles/create/가 실제 articles 폴더 안에 create 폴더 안을 나타내는 것은 아님
```

### Parameters
```
웹 서버에 제공하는 추가적인 데이터

파라미터는 '&' 기호로 구분되는 key-value 쌍 목록

서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
```

### Anchor
```
리소스의 다른 부분에 대한 앵커

리소스 내부 일종의 "북마크"를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시
    - 예를 들어 HTML 문서에서 브라우저는 앵커가 정의한 지점으로 스크롤 함

fragment identifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송되지 않음
    - 예를 들어 https://docs.djangoproject.com/en/3.2/intro/install/#quick-install-guide 요청에서 #quick-install-guide는 서버에 전달되지 않고 브라우저에 해당 지점으로 이동할 수 있도록 함
```


# 정리
- 웹에서의 리소스 식별
    - 자원의 식별자 (URI)
        - 자원의 **위치**로 자원을 식별(URL)
        - 교유한 **이름**으로 자원을 식별(URN)

# REST API


### API
```
Application Programming Interface

애플리케이션과 프로그래밍으로 소통하는 방법
    - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성

API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공
    - 예를 들어 집의 가전 제품에 전기를 공급해야 한다고 가정해보자.
    - 우리는 그저 가전제품의 플러그를 소켓에 꽂으면 제품이 작동함
    - 중요한 것은 우리가 가전 제품에 전기를 공급하기 위해 "직접 배선을 하지 않는다는 것"
    - 이는 매우 위험하면서도 비효율적인 일
```

### Web API
```
웹 서버 또는 웹 브라우저를 위한 API

현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 Open API를 활용하는 추제

대표적인 Third Party Open API 서비스 목록
    - Youtube API
    - Naver Papago API
    - Kakao Map API

API은 다양한 타입의 데이터를 응답
    - HTML, XML, "JSON" 등
```

### REST
```
Representational State Transfer

API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
    - 2000년 로이 필딩이 박사학위 논문에서 처음으로 소개 된 후 네트워킹 문화에 널리 퍼짐

'소프트웨어 아키텍쳐 디자인 제약 모음'
(a group of software architecture design constraints)

REST 원리를 따르는 시스템을 "RESTful" 하다고 부름

REST의 기본 아이디어는 리소스 즉 자원
    - "자원을 정의하고 자원에 대해 주소를 지정하는 전반적인 방법을 서술"
```

### REST에서 자원을 정의하고 주소를 지정하는 방법
1. 자원의 식별
    - URI
2. 자원의 행위
    - HTTP Method
3. 자원의 표현
    - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
    - JSON으로 표현된 데이터를 제공

### JSON
```
JSON is a lightweight data-interchange format

JavaSript의 표기법을 따른 단순 문자열

파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 "key-value 형태의 구조"를 갖고 있음

사람이 읽고 쓰기 쉽고 기계가 파싱(해석 & 분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입
```

# REST 정리
- 자원을 정의하고 자원에 대한 주소를 지정하는 방법의 모음

1. 자원을 식별 - URI

2. 자원에 대한 행위 - HTTP Methods

3. 자원을 표현 - JSON

- 설계 방법론을 지키지 않았을 때 잃는 것보다 지켰을 때 얻는 것이 훨씬 많음
    - 단, 설계 방법론을 지키지 않더라도 동작 여부에 큰 영향을 미치지는 않음
    - 말 그대로 방법론일 뿐이며 규칙이나 규약은 아님