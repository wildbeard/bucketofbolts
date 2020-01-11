#!/usr/bin/env sh

cd /var/www/bucketofbolts

pip install -r requirements.txt

# can only access if --host=0.0.0.0 is set
env FLASK_APP=bucketofbolts-api.py flask run --host=0.0.0.0