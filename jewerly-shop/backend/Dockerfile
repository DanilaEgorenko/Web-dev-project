FROM python:3.9

ENV PYTHONUNBUFFERED=1

ADD ./ /

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

RUN python manage.py migrate