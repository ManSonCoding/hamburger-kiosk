# hamburger-kiosk

##햄버거 키오스크

```bash
# Clone this repository
git clone https://github.com/ManSonCoding/hamburger-kiosk
# Go into the repository
cd hamburger-kiosk

#kiosk 폴더 압축을 푸시고
unzip hamburger-kiosk.zip

#한번 더 디렉토리 이동
cd hamburger-kiosk

# Install dependencies and run the app
npm install && npm start
```

## 카카오페이 기능은 장고 서버 동작 필요
```bash
pip install django 

pip install django-debug-toolbar

cd django_rest

# 현재 디렉토리에 manage.py있는지 확인
cd ls

# 장고 서버 실행
python manage.py runserver 


```

## 현재 구현해야 하는 기능
- dialogflow node js 에서 동작
- 채팅 UI 'DialogFlow-Chatbot-web-SDK-master' 와 같이 구현
- DB연동
- 장고 서버 배포
