#/bin/bash
docker run -d --name lecture_models -p 5555:5432 -e POSTGRES_USER=app -e POSTGRES_PASSWORD=123 -e POSTGRES_DB=models postgres
python3 manage.py makemigrations
python3 manage.py migrate
