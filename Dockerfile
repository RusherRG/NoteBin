FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /notebin
WORKDIR /notebin

ADD . /notebin/

RUN pip install  --no-cache-dir -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
