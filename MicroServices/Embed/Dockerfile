FROM python:3.9.18-slim-bullseye
WORKDIR /srv/
COPY ./requirements.txt /srv/
COPY ./app /srv/app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /srv/requirements.txt
COPY ./run.sh /srv/run.sh
RUN chmod +x /srv/run.sh
CMD ["/srv/run.sh"]