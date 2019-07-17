FROM python:3

WORKDIR /usr/src/app

# ENV DEBUG=false

COPY requirements.txt ./
COPY requirements.prod.txt ./

RUN pip install --no-cache-dir -r requirements.txt  -r requirements.prod.txt

COPY . .

# CMD [ "gunicorn", "smart_policy_task.wsgi:application", "-b", "0.0.0.0:8000" ]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]