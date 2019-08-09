```bash
# install virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install --no-cache-dir -r requirements.txt

# install development dependencies
pip install --no-cache-dir -r requirements.dev.txt

# migrate
python manage.py migrate

# run serve
python manage.py migrate
```

## Using docker-compose

```bash
docker-compose up --build -d
docker-compose exec django python manage.py migrate
```




IC

from .base import env, DATABASES


DEBUG = True


DATABASES['default'] = env.db('DATABASE_URL', engine='django_db_geventpool.backends.postgresql_psycopg2',
                            default='pgsql://nderyushev:bullet115@127.0.0.1/integrationcore')
DATABASES['default']['CONN_MAX_AGE'] = 0
DATABASES['default']['OPTIONS'] = {
    'MAX_CONNS': 85,
}

MICRO_DICT_URL = 'http://dicts.qa.agentapp.ru/v1'


PS

from .base import env, DATABASES, INSTALLED_APPS

ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES['default'] = env.db('DATABASE_URL', engine='django_db_geventpool.backends.postgresql_psycopg2',
                              default='pgsql://nderyushev:bullet115@127.0.0.1/partnerstore')
DATABASES['default']['CONN_MAX_AGE'] = 0
DATABASES['default']['OPTIONS'] = {
    'MAX_CONNS': 100,
}


MICRO_DICT_URL = 'http://dicts.qa.agentapp.ru/v1'
MICRO_INTEGRATIONCORE_URL = 'http://127.0.0.1:8010/v1'
RSA_MICROSERVICE_URL = 'http://rsa-micro.srv8.agentapp.ru'
RSA_MICROSERVICE_TOKEN = 'MegarussD-15'
BILLING_URL = 'http://localhost:8010'

INSTALLED_APPS += ('django_extensions', )

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = True

CELERY_TASK_ALWAYS_EAGER = True
