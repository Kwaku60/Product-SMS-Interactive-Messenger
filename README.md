# Running Application lcoally

# installation

pipenv shell
pipenv install
$python
from app import db
db.create_all()

# running

navigate to the api directory:
python run.py

navigate to the app directory:
npm install
npm start

# Running Application on Docker

docker-compose build
docker-compose up

Note: Need to get the db created in docker, ran into issues, appliations serves, but endpoints fail in docker environment as a result.

#####
