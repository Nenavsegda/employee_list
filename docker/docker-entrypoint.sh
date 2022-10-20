#!/bin/bash

>&2 echo "Waiting for PostgreSQL"

/var/www/Shop-manager/wait-for-it.sh  -h "db" -p "5432" -t 10 -- >&2 echo "PostgreSQL is ready"
python3 manage.py migrate
python3 manage.py populatedb
python3 manage.py runserver 0.0.0.0:8000
