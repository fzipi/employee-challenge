# Container challenge

The docker installation of the Python Flask app uses the approach that each container has a defined duty, and may be ephemeral in time.

Containers should be easy to orchestrate to serve our needs: they can be scaled, created, or destroyed to support the business needs. Based on the twelve factor app[^2] concepts, I used environment variables for configuring the application or containers as needed.

As required for this challenge, I based the containers in the official ubuntu 16.04 image.

To orchestrate a simple network with two containers, I used `docker-compose`[^1].

- The db container has the MySQL database, which is provisioned with the data from the `test_db`.
- The nginx container has the Nginx Web Server, along with the uWSGI service running the python-flask app to show the required data.

Tipically, you use the container for a single application. One could argue that the nginx container could be split in two, to give each container a single duty and to allow the Nginx frontend container to scale. For simplicity, I used only one for the web server *and* the application server.

Usually, official images are used for applications in containers. Personally, I always try to use the alpine linux images, which are arguably the smallest and fastest images for containers.

To build the containers, download docker-compose. In Ubuntu, use `apt-get install -y docker-compose`.

Afterwards, use:

```
docker-compose build
```
And to run the example, use:
```
docker-compose up
```
Then [go to this page](http://localhost) to show the flask application.

Read next the extended documentation on the creation and rationale of each container.

## The MySQL container

This container is based on the ubuntu 16.04 image.

I followed these steps to provision the database:

1. Install the database using `apt-get`.
2. Start the database.
  For this step I modified the official `docker-entrypoint.sh` from the MySQL image. I used environment vars to create the user and the database for the application.
  There is an special behavior in the docker entrypoint, which imports all the `.sql` files found in the `docker-entrypoint-initdb.d` directory. Therefore, the `test_db` files are there.

## The Nginx + App Server

This container is based on the ubuntu 16.04 image.

I needed to configure the nginx server to proxy all traffic to the uWSGI python-flask app. As this container executes two daemons, I used `supervisor`[^3] to start Nginx and gunicorn[^4] to serve the Python-Flask App.

The steps followed in this case were:

1. Install Nginx, supervisor, and python-pip.
2. Install Python-Flask requirements.
3. Copy the supervisor configuration, and prevent the Nginx daemon from starting (it will be launched by supervisor).
4. Run supervisor.


[^1]: https://github.com/docker/compose
[^2]: https://12factor.net/
[^3]: http://supervisord.org/
[^4]: http://gunicorn.org/
