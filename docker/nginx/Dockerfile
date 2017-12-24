FROM ubuntu:16.04

MAINTAINER Felipe Zipitria <fzipi@fing.edu.uy>

ENV TERM ansi

# Install base packages. mysqlclient-dev is needed for Flask MySQLdb
RUN apt-get update \
 && apt-get install -y python-pip \
    python-virtualenv \
    nginx-full \
    libmysqlclient-dev \
    curl \
    supervisor \
 && apt-get remove --purge -y $BUILD_PACKAGES \
 && rm -rf /var/lib/apt/lists/*

# Copy our app inside the container
COPY app /app
COPY employees.cfg /app/production.cfg

# Install requirements
RUN pip install -r /app/requirements.txt

# Custom Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/flask.conf

# Copy nginx uwsgi config
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY app.conf /etc/nginx/sites-available/default
# Run forest, run!

# Forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

STOPSIGNAL SIGTERM

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
#CMD uwsgi -s /tmp/employees.sock --uid www-data --gid www-data \
#          --manage-script-name --chdir /var/www --mount /=employees:app

EXPOSE 80
