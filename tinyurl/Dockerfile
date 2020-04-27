FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/requirements.txt

# Install build dependencies to compile uWsgi. Remove compilation dependencies once done to keep image size small.
RUN set -ex \
    && buildDeps='gcc \
        libbz2-dev' \
    && apt-get update && apt-get install -y $buildDeps && rm -rf /var/lib/apt/lists/* \
    && pip3 install uwsgi \
    && apt-get purge -y --auto-remove $buildDeps \
    && find /usr/local -depth \
    \( \
        \( -type d -a -name test -o -name tests \) \
        -o \
        \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    \) -exec rm -rf '{}' +

# Install framework and utilizies
RUN pip3 install -r requirements.txt

# Copy app files
ADD . /app

# Expose port to docker network alone
EXPOSE 5000

CMD uwsgi --ini uwsgi.ini