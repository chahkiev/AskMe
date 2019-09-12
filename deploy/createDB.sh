#!/bin/bash

sudo apt-get -y update
sudo apt-get install -y postgresql && \
                postgresql-contrib && \
                python-psycopg2 && \
                libpq-dev 

sudo -u postgres psql -f ./config.sql