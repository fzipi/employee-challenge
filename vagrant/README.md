# Ansible and Vagrant Challenge

For any playbook/module/cookbook you usually need to evaluate the best option between support/downloads/documentation and your needs. I chose the roles from the Ansible Galaxy[^1] that suited my needs: one for the MySQL installation, and the other for the Nginx server.

In this example, I used Vagrant[^2] with the Ansible[^3] provider. I used Ansible version 2.4, which is what I have in my Fedora 27 Workstation.

The role I created, `fzipi.flask_app`, installs the application and provisions the data into the database. It is complemented by two roles from the Ansible Galaxy: `wtanaka.mysql` and `jdauphant.nginx`.

To execute the Python-Flask application, I used the gunicorn[^4] uWSGI server. Additionally, I created a systemd service file for running the uWSGI service.

To generate the Ubuntu 16.04 VM provisioned with MySQL, Nginx, and the Python-Flask App, execute:
```
sudo vagrant up
```
The `Vagrantfile` has these properties for the resulting VM to:

- Be based on the 'ubuntu/xenial64'
- Install required roles from the Galaxy
- Install Python needed for Ansible
- Provision using Ansible the needed services
- Configure a port forwarding from 8080 on the host, to port 80 on the guest
  As you may have port 8080 already forwarded or in use, I've added `auto_correct: true` for the `config.vm.networ "forward_port"`, so at VM boot it will inform you about the free port mapping chosen for the forwarding.

Now you can [access the application](http://localhost:8080) on localhost port 8080 (or whatever port has been selected by the vagrant runtime).

[^1]: https://galaxy.ansible.com/
[^2]: https://www.vagrantup.com/
[^3]: https://www.ansible.com/
[^4]: http://gunicorn.org/
