# Set Up

general steps for local development and updating the webserver

## local

git clone or pull from `mlr/weather/<branch>`

make `venv` and `pip install dev-requirements.txt`

run tests with with `python -m pytest tests/` from project root 

run app locally with `python app.py` or `gunicorn --workers=2 app:app`

make a new branch for an issue and develop against it

run tests locally after changes and push to remote branch

on push to remote branch a CI runner will run tests

on merge from branch to master a CI runner will run tests

tests are the same for local and CI runner

## webserver

login to server via `ssh` and check for updates

`nginx` web server and `gunicorn` wsgi are managed with `systemctl`

app runs as a service with `systemd` with same setup as local

to update app `git pull` latest from remote `mlr/weather/master`

reload service with `systemctl deamon-reload`

restart service with `systemctl restart app.service`

