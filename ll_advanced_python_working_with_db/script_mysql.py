#####################################
# setup
'''
$ mysql -u root -p
mysql> create database projects;
mysql> use projects;
mysql> create  table projects (project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id));
mysql> create table tasks(task_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255)
, PRIMARY KEY(task_id), FOREIGN KEY(project_id) REFERENCES projects(project_id));

mysql> insert into projects(title, description) values("Organize Photos", "Organize old iphone photos by year");

mysql> insert into tasks(project_id, description) values(1, "Organize 2020 photos");

mysql> insert into tasks(project_id, description) values(1, "Organize 201 photos");

mysql> insert into projects(title, description) values("Read More", "Read a book a month this year");

mysql> insert into tasks(project_id, description) values(2, "Read 'The Huntress'");

$ pip install mysql-connector-python
'''

#####################################
# connecting
import mysql.connector as mysql
from dotenv import dotenv_values

db_config = dotenv_values(".env")

def connect(db_name):
    try:
        return mysql.connect(host="localhost", user="root", password=db_config["PW"], database="projects")
    except Error as e:
        print(e)

if __name__ == '__main__':
    db = connect("projects")
    cursor = db.cursor()
    cursor.excute(query)
    records = cursor.fetchall()
    print(records)

    db.close()

#####################################
# using function - simple
def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute('''INSERT INTO projects(title, description) VALUES(%s, %s)''', project_data)
    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)

    cursor.executemany('''INSERT INTO tasks(project_id, description) VALUES(%s, %s)'''. tasks_data)

#####################################
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, select
from sqlalchemy.orm import registry, relationship, Session

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/projects', echo=True)

mapper_registry = registry()
# mapper_registry.metadata

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title='{0}', description='{1}')".format(self.title, self.description)


class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))

    # this relationship is for the models
    project = relationship("Project")

    def __repr__(self):
        return "<Task(description='{0}')".format(self.description)

# sqlalchemy wll not create new ones if already existing
Base.metadata.create_all(engine)

# Sessions is how we create Transactions
with Session(engine) as session:
    organize_closet_project = Project(title='Organize closet', description='Organize closet by color and style')

    session.add(organize_closet_project)

    # to get the project_id, we need to flush
    session.flush()

    tasks = [
        Task(project_id=organize_closet_project.project_id, description='Decide what clothes to donate'),
        Task(project_id=organize_closet_project.project_id, description='Organize summer clothes'),
        Task(project_id=organize_closet_project.project_id, description='Organize winter clothes'),
    ]

    session.bulk_save_objects(tasks)
    session.flush()
    session.commit()

# to retrieve it, we also use Session
with Session(engine) as session:
    smt = select(Project).where(Project.title == 'Organize closet')
    results = session.execute(smt)
    organize_closet_project = results.scalar()

    # note how flush is not needed here
    smt = select(Task).where(Task.project_id == organize_closet_project.project_id)
    results = session.execute(smt)
    for task in results:
        print(task)
    

#####################################
# this is to use some SQL functions inside python
from sqlalchemy import func

max_query = select(func.max(Sales.order_total))
session.execute(max_query).scalar()

results_query = select(Sale).order_by(Sale.order_total.desc())
results_in_order = session.execute(results_query)
for order in results_in_order:
    print(order)
#####################################



    
