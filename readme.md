# Set Up

## local

git clone or pull from mlr/weather

make venv and pip install dev-requirements.txt

run tests with with python -m pytest tests/ from project root weather/

run app locally with python app.py or gunicorn --workers=2 app:app

make new branch for an issue and develop against it

run tests after changes and push to remote branch at mlr/weather

on push to remote branch same tests will run in a CI runner

on merge to master test in CI runner will run again

## linode vps

login to server via ssh and check for updates

nginx web server and gunicorn wsgi are installed and managed with systemctl

app is ran as a service with systemd and follows same setup as local

to update app pull latest from master and restart systemd service

## issues
