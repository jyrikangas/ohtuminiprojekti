#!/bin/bash

# käynnistetään Flask-palvelin taustalle
cd src
poetry run flask run &

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000)" != "200" ]];
  do sleep 1;
done

# suoritetaan testit
poetry run robot tests

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status
