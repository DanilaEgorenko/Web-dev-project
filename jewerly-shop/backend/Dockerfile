FROM python:3.9

WORKDIR /root/server
ADD ./ /root/server/

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

RUN python manage.py migrate