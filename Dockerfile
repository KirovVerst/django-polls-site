FROM python:3.8 as polls_image
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD polls_service/ /app/
RUN python manage.py migrate
