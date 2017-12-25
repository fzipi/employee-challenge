# Welcome to my challenge solving repo!

These repository contains the files for solving this challenge:

> Deploy a simple app that outputs the list of employees that are Male whose birth date is 1965-02-01 and the hire date is greater than 1990-01-01 ordered by the Full Name of the employee.
>  You will have to use Ubuntu 16.04 LTS as starting base and the solution needs to have the following items:
>
>  - NGINX web server
>  - Any programming language (PHP/Python/Perl/Whatever).
>  - MySQL server
>  - Configuration Management tool for configuring server (You can use Saltstack/Ansible/Puppet/Chef, is allowed to use modules/formulas/cookbooks from others so you don't reinvent the wheel but please don't do copy&paste solutions or use things like PuPHPet).

After weighing the posibilities, I created the application using the Flask[^1] microframework for Python. Once the application was functional, it was time for the deployment phase. I followed two approaches:

 - Use `docker-compose`[^2] for orchestrating two containers, one with the database and the other with the Web and Application Server.
  [Description here](docker/README.md)
 - Use `Vagrant`[^3] and create a VM with all the required services in it.  
   [Description here](vagrant/README.md)

To run both solutions:

1. Clone this repository, and its submodules. It will take a while.
```
git clone --recursive https://github.com/fzipi/employee-challenge.git
```
2. (Optional) If you don't have it, install `docker-compose` using your package manager. e.g.
```
apt-get install -y docker-compose
```
3. In the `docker` directory, execute
```
sudo docker-compose build
sudo docker-compose up
```
4. Go to `http://localhost` to test the app. End the test with `Ctrl+C`.
5. (Optional) If you don't have it, install `vagrant` using your package manager.
e.g.
```
apt-get install -y vagrant
```
6. In the `vagrant` directory, execute
```
sudo vagrant up
```
7. Go to `http://localhost:8080` to test the app.

That's all!

Felipe.

[^1]: https://flask.pocoo.org
[^2]: https://github.com/docker/compose
[^3]: https://www.vagrantup.com/
