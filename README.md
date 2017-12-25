# Welcome to my challenge solving repo!

These repository contains the files for solving this challenge:

> Deploy a simple app that outputs the list of employees that are Male which birth date is 1965-02-01 and the hire date is greater than 1990-01-01 ordered by the Full Name of the employee.
>  You will have to use Ubuntu 16.04 LTS as starting base and the solution needs to have the following items:
>
>  - NGINX web server
>  - Any programming language (PHP/Python/Perl/Whatever).
>  - MySQL server
>  - Configuration Management tool for configuring server (You can use Saltstack/Ansible/Puppet/Chef, is allowed to use modules/formulas/cookbooks from others so you don't reinvent the wheel but please don't do copy&paste solutions or use things like PuPHPet).

After weighting the posibilities, I began with the development of the application which queries the database and obtain the required data.

The application was created using the Flask[^1] microframework for Python. After having the application functional, its time for the deployment phase.

I followed two approaches:

 - Use `docker-compose`[^2] for orchestrating two containers, one with the database and the other with the Web and Application Server.
 - Use `Vagrant`[^3] and create a VM with all the required services in it.

The former approach is described [here](docker/README.md), and the latter is [here](vagrant/README.md).

The summary for testing both approaches is:

1. Clone this repository, and its submodules `git clone --recursive https://github.com/fzipi/employee-challenge.git`. It will take a while.
3. Go into the `docker` directory. Install `docker-compose` if you don't have it (```apt-get install -y docker-compose```), using your package manager.
   - Execute `sudo docker-compose build` and `sudo docker-compose up`. Go to `http://localhost` for testing the app.
   - End the test with `Ctrl+C`.
4. Go into the `vagrant` directory. Install `vagrant` if you don't have it (```apt-get install -y vagrant```), using your package manager.
   - Execute `sudo vagrant up`. Go to `http://localhost:8080` for testing the app.

That's all!

Felipe.

[^1]: https://flask.pocoo.org
[^2]: https://github.com/docker/compose
[^3]: https://www.vagrantup.com/
