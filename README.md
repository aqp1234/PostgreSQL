# PostgreSQL
 가상환경 설정 후 순서대로 진행
 가상환경 설정 방법
 1. visual code 의 cmd terminal을 이용하여 PostgreSQL 폴더로 이동
 2. venv\Scripts\activate.bat 입력
 3. set FLASK_APP=pyapi 입력
 
 
1. csv파일을 PostgreSQL폴더에 추가
2. visual code 의 cmd terminal을 이용하여 python tuning.py 실행
3. config.py, insert.py, createdatabase 의 SQLALCHEMY_DATABASE_URI의 user, pw를 자신에 맞게 설정
4. 2번의 cmd 창에서 python createdatabase.py 입력
5. flask db init 입력
6. flask db migrate 입력
7. flask db upgrade 입력
8. python insert.py 입력
9. flask run 입력
10. 127.0.0.1:5000 접속하여 127.0.0.1:5000/person/total 등 api 주소 접속하여 확인