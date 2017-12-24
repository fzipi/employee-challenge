from flask_table import Table, Col
from flask_mysqldb import MySQL
from flask import current_app

#CREATE TABLE employees (
#    emp_no      INT             NOT NULL,
#    birth_date  DATE            NOT NULL,
#    first_name  VARCHAR(14)     NOT NULL,
#    last_name   VARCHAR(16)     NOT NULL,
#    gender      ENUM ('M','F')  NOT NULL,
#    hire_date   DATE            NOT NULL,
#    PRIMARY KEY (emp_no)
#);
# Declare your table
class EmployeeTable(Table):
    classes=['table', 'table-striped']
    emp_no = Col('Employee#')
    birth_date = Col('Birth Date')
    first_name = Col('Name')
    last_name = Col('Surname')
    gender = Col('Gender')
    hire_date = Col('Hired in')

    
class Employee(object):
    def __init__(self, emp_no, birth_date, first_name, last_name, gender, hire_date):
        self.emp_no = emp_no
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hire_date = hire_date
        

# The database!
db = MySQL()

def get_employees():
    """
    Query: the list of employees that are Male which birth date is 1965-02-01
        and the hire date is greater than 1990-01-01
        ordered by the Full Name of the employee
    """
    with current_app.app_context():
        conn = db.connect

    cursor = conn.cursor()
    query = '''SELECT * FROM employees WHERE gender = 'M' AND birth_date = '1965-02-01' AND hire_date > '1990-01-01' ORDER BY first_name,last_name'''
    try:
        cursor.execute(query)
        data = cursor.fetchall()            
    except MySQLdb.Error as e:
        raise
    finally:
        cursor.close()
    conn.close()
    
    employees = []
    for row in data:
        employees.append(Employee(row[0],row[1],row[2],row[3],row[4],row[5]))

    # Populate the table
    table = EmployeeTable(employees)
    return table
