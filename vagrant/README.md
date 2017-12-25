# Ansible and Vagrant Challenge

Usually, for any playbook/module/cookbook, you need to evaluate the best option between support/downloads/documentation and your needs. I choose the roles from the galaxy that matched my needs; one for the mysql installation, and the other for the nginx server.

I will be using `vagrant` in this example, with the ansible provider.

In this example, I am using `ansible` version 2.4, which is what I have in my Fedora 27 Workstation.

The role `fzipi.flask_app` will use two roles from the galaxy, namely `wtanaka.mysql` and `jdauphant.nginx`. that are documented in the `requirements.yml`. The role I created installs the application and provisions the data into the database.

For executing the Python-Flask application, I choose `gunicorn` and created a systemd service file for running the wsgi server.

Now you just need to execute `sudo vagrant up` for generating the ubuntu 16.04 VM provisioned with MySQL, nginx, and the python-flask App.

Our `Vagrantfile` has these properties:

- Based on the 'ubuntu/xenial64'.
- Installs required roles from the galaxy.
- Installs `python` needed for Ansible.
- Provisions using ansible the needed services.
- Configures a port forwarding from 8080 on the host, to port 80 on the guest. As you may have port 8080 already forwarded or in use, I've added `auto_correct: true` for the `config.vm.networ "forward_port"`, so at boot it will inform you about the free port mapping chosen for the forwarding.

Now you can [access the application](http://localhost:8080) on localhost port 8080 (or whatever port has been selected by the vagrant runtime).
