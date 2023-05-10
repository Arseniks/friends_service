FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /friends_service

COPY . /friends_service

RUN pip install -r /friends_service/requirements/requirements.txt
RUN pip install -r /friends_service/requirements/requirements_dev.txt
RUN pip install -r /friends_service/requirements/requirements_test.txt

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]