# Employee List

# Installation

```
sudo apt-get install -y python-pip libmysqlclient-dev
git clone <this repo>
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

For testing:

```
flask --app=app -c (pwd)/default_config.py 
```

You will need access to the database configured in `default_config.py` for this to show the query result.

For production use you will need `gunicorn` or another `uwsgi` server for high performance.
