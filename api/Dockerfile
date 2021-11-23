FROM python:3.7

# set work directory
WORKDIR /opt/api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV development
ENV FLASK_DEBUG 1
ENV FLASK_APP run.py
ENV SQLALCHEMY_DATABASE_URI postgresql+psycopg2://postscript:dev@db/postscript

# install postgres client
RUN apt update && \
      apt install postgresql-client -y && \
      rm -rf /var/cache/apt/archives

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
# Run pip install flask-marshmallow
# RUN pip install flask-cors 
# RUN pip install twilio

COPY ./Pipfile .
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pipenv install --system --skip-lock --dev --deploy
# RUN pipenv install flask 
# RUN pipenv install flask-marshmallow
# RUN pipenv install flask-cors 
# RUN pipenv install twilio


# Setup a Development User
RUN useradd -ms /bin/bash postscript 
USER postscript

# copy project
COPY . .

# Run Commands
EXPOSE 5000
ENTRYPOINT ["/opt/api/cmds/entrypoint.sh"]
CMD ["python", "-m", "flask", "run", "--host=127.0.0.1"]
# CMD ["gunicorn", "--user=postscript", "--bind=0.0.0.0:5000", "run:app"]