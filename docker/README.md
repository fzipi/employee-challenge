# Container challenge

The docker installation of the Python Flask app uses the approach that each container has a defined duty, and may be ephemeral in time.

Containers should be easy to orchestrate to serve our needs: they can be scaled, created, or destroyed to support the business needs. Furthermore, using the twelve factor app[^2] concepts, we should use environment variables for configuring our application or containers as needed.

So, the normal use will be just to use the container for the application needed, e.g. use the container for MySQL server, regarding the underlying OS. And choose an official image for that. In my case, I always try to use the alpine linux images, which are arguably the smaller and faster images for containers.

For the sake of this challenge, we based our containers in the official ubuntu 16.04 image.

For orchestrating a simple network with two containers, we used `docker-compose`[^1]. Both containers have been installed using the `ubuntu:16.04` base image. They have:
- The MySQL database, which is provisioned with the data from the `test_db`.
- The Nginx Web Server, along with the uWSGI service running the python-flask app to show the required data.

One could argue that this last container could be splitted in two, for further dividing the duties of each container, and allowing to scale the Nginx frontend container. For the sake of simplicity, we will use only one for the web server *and* the application server.

For building the containers, you will need to download docker-compose. In Ubuntu, use `apt-get install -y docker-compose`. Afterwards, use

```
docker-compose build
```
And for running the example, use:
```
docker-compose up
```
Then browse [here](http://localhost) to show the flask application.

Read next the extended documentation on each container creation and rationale.

## The MySQL container

This container, as we said, is based on the ubuntu 16.04 image.

The steps for its creation were:

- Install the database.
  Using apt-get.
- Starting the database.
  For this step we modified the official `docker-entrypoint.sh` from the MySQL image. There was no need to re-create something in this step, just initialize the database.
  We used environment vars to create the user and the database for our application.
  There is an special behavior in the docker entrypoint, which will import all the `.sql` files found in the `docker-entrypoint-initdb.d` directory. Therefore the `test_db` files are there.

These steps worked for provisioning our database.

## The Nginx + App Server

The Nginx container is based on the ubuntu 16.04 image also.

We need to configure the nginx server to proxy all traffic to our uWSGI python-flask app. As this container will be executing two daemons, we used `supervisor`[^3] for starting Nginx and the gunicorn[^4] server to server our Python-Flask App.

The steps followed in this case were:

- Install Nginx, supervisor, and python-pip.
- Install Python-Flask requirements.
- Install supervisor configuration, and disable Nginx daemon from start (will be launched by supervisor)
- Run supervisor.


[^1]: https://github.com/docker/compose
[^2]: https://12factor.net/
[^3]: http://supervisord.org/
[^4]: http://gunicorn.org/
