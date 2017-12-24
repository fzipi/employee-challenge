# Welcome to my challenge solving repo!

These repository contains the files for solving this challenge:

> Deploy a simple app that outputs the list of employees that are Male which birth date is 1965-02-01 and the hire date is greater than 1990-01-01 ordered by the Full Name of the employee.
>  You will have to use Ubuntu 16.04 LTS as starting base and the solution needs to have the following items:
>
>  - NGINX web server
>  - Any programming language (PHP/Python/Perl/Whatever).
>  - MySQL server
>  - Configuration Management tool for configuring server (You can use Saltstack/Ansible/Puppet/Chef, is allowed to use modules/formulas/cookbooks from others so you don't reinvent the wheel but please don't do copy&paste solutions or use things like PuPHPet).

After weighting the posibilities, I decided to first create the application for querying the database.

The application was created using the Flask[^1] microframework for python. After having the application functional, then come the deployment.

I followed two approaches:

 - Use docker-compose for orchestrating two containers, one with the database and the other with the Web and Application Server.
 - Use Vagrant and create a VM with all the required services in it.

The former approach is described [here](docker/README.md), and the latter is [here](vagrant/README.md).

The summary for testing both approaches is:

1. Clone this repository. `git clone https://github.com/fzipi/challenge.git`
2. Get the submodules: `cd challenge; git submodule init; git submodule update`
3. Go to `docker` directory. Install `docker-compose` if you don't have it.
   - Execute `docker-compose build` and `docker-compose up`. Go to `http://localhost` for testing the app.
   - End the test with `Ctrl+C`.
4. Go to `vagrant` directory. Install `vagrant` if you don't have it. 
   - Install required playbooks: `ansible-galaxy install -r requirements.yml --roles-path ./roles`
   - Execute `sudo vagrant up`. Go to `http://localhost:8080` for testing the app.

That's all!

[^1]: https://flask.pocoo.org
