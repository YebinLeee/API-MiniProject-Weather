# API-MiniProject-Weather
⛅ 공공 open API 활용 - 동네의 날씨 데이터 <br>

국내의 특정 지역에 해당하는 예보지점 (x,y) 좌표값을 입력하면 그 동네의 기온과 날씨를 알려준다.

- [설명](https://velog.io/@yebinlee/Python-API-%EC%8B%A4%EC%8A%B5)


<br>


## [Reference]
- [공공데이터 포털 - 기상청_동네 날씨 조회 데이터 API](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057682)
- [tistory blog : ai creator - 날씨 정보 사용 맛집 추천 프로젝트](https://ai-creator.tistory.com/31)

<br>
<hr>


### [Terminal 실행]

<img src="https://github.com/YebinLeee/API-MiniProject-Weather/blob/main/img/0523-1400.PNG" width=500>

- 05월 23일 약 16시 7분 실행 -> 14 시에 업데이트된 자료에 대한 날씨 데이터 확인
<br>

<img src="https://github.com/YebinLeee/API-MiniProject-Weather/blob/main/img/0523-2000.PNG" width=500>

- 05월 23일 약 21시 36분 실행 -> 20 시에 업데이트된 자료에 대한 날씨 데이터 확인 

<img src="https://github.com/YebinLeee/API-MiniProject-Weather/blob/main/img/0523-2000-3.PNG" width=500>

- 05월 23일 약 23시 06분 실행 -> 20 시에 업데이트된 자료에 대한 날씨 데이터 확인

<img src="https://github.com/YebinLeee/API-MiniProject-Weather/blob/main/img/0524-2300.PNG" width=500>

- 05월 24일 약 23시 26분 실행 -> 23 시에 업데이트된 자료에 대한 날씨 데이터 확인

<img src="https://github.com/YebinLeee/API-MiniProject-Weather/blob/main/img/0527-0800.PNG" width=500>

- 05월 27일 약 08시 44분 실행 -> 08 시에 업데이트된 자료에 대한 날씨 데이터 확인 (A rainy day ☔️)

<br><br>


### [추가 아이디어 / 추가 예정]

- [x] gitignore -> secret.json 파일 감추기
- [ ] 지역 검색해서 위도/경도 추출하는 API 이용 (kakao api 또는 googlemaps api의 geocoding 사용)
- [ ] 지도 map 이용 (kakao map api)
- [ ] 입력: 검색 bar
- [ ] 출력: 귀여운 날씨 아이콘(그림) 출력
- [ ] 미세먼지 데이터 api & 내일 일기예보 데이터
- [ ] 카카오톡 연결 (kakao service api) 
