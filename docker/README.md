# Container challenge

The docker installation of the Python Flask app uses the container concept that each container has a defined duty, and that container may be ephemeral in time.

Containers are created to be orchestrated in the way we need for serving our needs: they can be scaled, created, and destroyed as time goes on. Furthermore, if we base our development on the twelve factor app[^1], we  will use environment variables for configuring our application or containers as needed.

The normal use will be just to use the application needed, e.g. use the container for mysql regarding the underlying OS, and choose an official image for that. In my case, I always try to use the alpine linux images, which are arguably the smaller and faster images for containers.

For the sake of this challenge, we based our containers in the official ubuntu 16.04 image.

We use `docker-compose` for orchestrating a simple network with two containers. Both containers have been installed using the `ubuntu:16.04` base image. They have:
- the mysql database, and is provisioned with the data from the test_db
- the nginx Web Server, along with the uWSGI service with calls the python-flask app for showing the required data.

One could argue that this last container could be splitted in two, for further dividing the duties of each container, and allowing to scale the nginx frontend container. For the sake of simplicity, we choose to use only one for the web server and the application server.

For building the containers, just use:
```
docker-compose build
```
And for running the example, use:
```
docker-compose up
```
Then navigate to `http://localhost` to show the flask application.

Read next the extended documentation on each container creation and rationale.

## The MySQL container

This container, as we said, is based on the ubuntu 16.04 image.

The steps we followed are:

- install the database.
  this is simply using apt-get
- start the database
  for this step we modified the official `docker-entrypoint.sh` from the mysql image. There was no need to re-create something in this step, just initialize the database.
  We use a special behaviour from the entrypoint, which imports the `.sql` files founded in the `docker-entrypoint-initdb.d`. So the `test_db` files are there, previously removing superflous files that will not add nothing to the container.

These steps worked for provisioning our database.

## The Nginx + App Server

The nginx container is based on the ubuntu 16.04 image also.

We need to configure the nginx server to proxy all traffic to our uWSGI python-flask app.





[^1]: https://12factor.net/
