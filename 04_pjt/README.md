## [첫 번째] pk 주의!
![0](https://user-images.githubusercontent.com/104968672/188067206-3eec6d7d-e2de-4b5b-8b67-0668f633f9b4.JPG)

- url을 작성할 때 <int:pk>를 작성했음 그렇다면 넘겨줄 때 pk를 같이 넘겨줘야 하는데 그렇지 못해서 아래와 같은 오류가 발생함

![1](https://user-images.githubusercontent.com/104968672/188067448-c9511f7e-e1f7-4eff-863a-6e4416e94ae4.JPG)

- Reverse for 'detail' with no arguments not found. 즉, pk 값이 없음

![1-1](https://user-images.githubusercontent.com/104968672/188067608-a154176e-f2b4-4c51-84f9-b981f9b69c11.JPG)

```
<a href="{% url 'movies:detail' movie.pk %}">
# 빠졌던 movie.pk를 작성함
```
**느낀점:** pk가 왜 필요한 지 다시 생각해 볼 수 있었고, 어디서 빠지지는 않았는 지 잘 확인해야 함을 느꼈다.

## [두 번째] img tag 기억하기
- 포스터 이미지를 어떻게 받아 올 수 있을 지 고민하는 시간을 가졌었음

![3](https://user-images.githubusercontent.com/104968672/188068099-5c734231-c864-4bc0-ae5e-fbc7d7739cc1.JPG)

- 위와 같이 img tag를 사용해서 src에 입력해서 받아올 수 있었음
- 그런데 new.html에서 작서한 poster_url의 값을 이미지로 받아야 하는 것을 주의해야 함

**느낀점:** 앞서 배웠던 tag들 한번 더 복습할 필요가 잆음, src에 단순히 가져온 url을 입력하면 그거만 출력된다. 그러니 새로운 입력에 맞는 포스터를 출력하려면 어떻게 연결되는 지 생각하고 있어야 하고 여기서는 poster_url을 입력하라고 요구했기 때문에 그 값으로 넣어줘야 함

## [세 번째] Release_date와 Genre 구현하기

![2](https://user-images.githubusercontent.com/104968672/188068622-703c8c3c-75b8-4fc2-9b4f-79567368faaf.JPG)

- 처음에는 어떻게 구현할 지 몰라서 단순하게 text로 먼저 구현하고 CRUD를 작업 했음

![2-1](https://user-images.githubusercontent.com/104968672/188068802-6efe47b7-81e8-4027-805a-fea4c8ca08fe.JPG)

- Release_date는 type에 "date"로만 바꿔주면 되는,, 생각?보다 간단했음
- Genre의 경우 구글링을 통해 select를 알게 되었고 진우의 조력을 받아 기능을 구현할 수 있었음
- option으로 여러 선택지를 만들 수 있었음

![2-2](https://user-images.githubusercontent.com/104968672/188069118-452ab1b9-249d-4d67-9cf9-f80e58fb718f.JPG)

**느낀점:** 구글링 최고다.. 모르면 찾아보고 찾으면 있으니 구현할 수 있는 능력도 중요하다.

# [네 번째] pk 주의 또 주의!

![4](https://user-images.githubusercontent.com/104968672/188072392-362bef3e-f42d-4823-9147-e086cb41a1cc.JPG)

- edit, delete url을 넘겨줄 때 pk를 알아야 그거에 맞게 삭제를 하든, 수정을 하겠지?
- delete의 경우 action에 넣어줘야 한다.

**느낀점:** pk만 주의하면 될 거 같다. movies:index와 같이 pk없이 넘겨주는 것과 헷갈리지 말기

# [다섯 번째] reset, 초기화 어떻게 하지?

![5](https://user-images.githubusercontent.com/104968672/188073053-2b4e04a8-3e22-4305-a33b-f37a41cadec7.JPG)

- reset을 누를 경우 원래의 값으로 초기화 되어야 하기 때문에 처음에는 submit와 같이 다른 action에 넣어줘야 되나 생각했음
- 그럴 경우 해당 폼들이 한번씩 더 구현이 되길래 틀렸구나 생각하고 구글링해서 찾아봄
- 얻은 결과는 의외로 간단,, input type에 그냥 reset로 넣어주면 끝!

**느낀점:** action과 같이 코드를 짰을때 어떻게 될 지 미리 알 수 있는 능력을 키우면 좋겠고, 일단 너무 어렵게 생각하는 걸 버릴 필요가 있을 듯,, 해결책은 생각보다 간단할 수 있다!!