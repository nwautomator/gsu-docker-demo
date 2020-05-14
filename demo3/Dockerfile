FROM debian:buster
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip build-essential libmariadbclient-dev
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10
RUN pip install Flask flask_cors mysql-connector-python gunicorn
EXPOSE 8001
VOLUME /code
WORKDIR /code
COPY *.py /code/
RUN mkdir /code/templates
COPY templates* /code/templates/
CMD ["gunicorn", "--log-level", "debug", "--workers=20", "-b 0.0.0.0:8001", "demo:app"]
