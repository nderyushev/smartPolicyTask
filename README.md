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




