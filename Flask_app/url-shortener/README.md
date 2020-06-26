### Active
```
$ pipevn shell
```
### Exit the virtualenv
```
$ exit
```
### Command Line Interface
- The `FLASK_APP` environment variable is used to specify how to load the application.
```
$ export FLASK_APP=urlshort
```
```
$ export FLASK_ENV=development
```
### Run App
```
$ flask run
```
- Run publicly
```
$ flask run --host=0.0.0.0
```
### Run Testing
```
$ pytest
```
## Deploy
```
$ pipenv install gunicorn
```
```
$ gunicorn "urlshort:create_app()" -b 0.0.0.0
```
```
$ sudo apt install nginx
$ systemctl status nginx
```
