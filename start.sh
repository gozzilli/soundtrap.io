#!/bin/bash

if [ -f /usr/local/var/postgres/postmaster.pid ]
then
    echo postgres already running
else
    postgres -D /usr/local/var/postgres &
fi

source venv-mac/bin/activate

echo -n "Run server? [y/N] "
read doRunserver
if [[ ${doRunserver,,} == "y" ]]; then
	./manage.py runserver
fi 
