FROM python:3.8 as polls_image
RUN mkdir /app
WORKDIR /app

# install requirements
RUN pip install -U pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY polls_service/ /app/
RUN python manage.py migrate
