# Ansible and Vagrant

Usually, for any playbook/module/cookbook, you need to evaluate the best option between support/downloads/documentation and your needs. I choose the roles from the galaxy that matched my needs; one for the mysql installation, and the other for the nginx server.

Our application is a Python-Flask, connected with WSGI to nginx, and reading data from a MySQL database.

I will use for this example `vagrant` with the ansible provider.

In this example, I am using `ansible` version 2.4, which is what I have in my Fedora 27 Workstation.

The role `fzipi.flask_app` will use two roles from the galaxy, and are documented in the `requirements.yml`. This role installs the application and provisions the data into the database.

For executing the flask application, I decided to use `gunicorn` and created and systemd service file for executing the wsgi server.

The first step is to install the required modules, using `ansible-galaxy`:

```
ansible-galaxy install -r requirements.yml --roles-path ./roles
```

After downloading the required roles to the local filesystem, execute `sudo vagrant up` for generating the ubuntu 16.04 VM provisioned with MySQL, nginx, and our python-flask app.

Our `Vagrantfile` does this:

- Based on the 'ubuntu/xenial64'
- Installs `python` needed for Ansible
- Provisions using ansible the needed services
- Configures a port forwarding from 8080 on the host, to port 80 on the guest.

Now you can acces the application on localhost port 8080.
