web: gunicorn project_gyminy:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate