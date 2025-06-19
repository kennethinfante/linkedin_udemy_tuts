# using sqlite
import sqlite3

con = sqlite3.connect('movies.db')

cur = con.cursor()

# sqlite does not have date data type
cur.execute('''
    create table if not exists Movies (Title TEXT, Director TEXT, Year INT)
    ''')

con.commit()
con.close()

#####################################
cur.execute('''
    INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976)
    ''')

cur.execute('''
    SELECT * FROM Movies
    ''')

cur.fetchone()
#####################################
famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
('Back to the Future', 'Robert Zemeckis', 1985),
('Moonrise Kingdom', 'Wes Anderson', 2012)
]

cur.executemany('INSERT INTO Movies VALUES (?, ?, ?)', famousFilms)
cur.execute('''
    SELECT * FROM Movies
    ''')

cur.fetchall()
#####################################
release_year = (1985, )

cur.execute("SELECT * FROM Movies WHERE year=?", release_year)

cur.fetchall()

#####################################
# sqlalchemy 2
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

with engine.connect() as conn:
    query = sqlalchemy.text("SELECT * FROM Movies")
    results = conn.execute(query)
    for row in results:
        print(row)

#####################################
# sql expression language
metadata = sqlalchemy.MetaData()

movies_table = sqlalchemy.Table("Movies", metadata,
                    sqlalchemy.Column("title", sqlalchemy.Text),
                    sqlalchemy.Column("director", sqlalchemy.Text),
                    sqlalchemy.Column("year", sqlalchemy.Integer),
                    )

metadata.create_all(engine)

with engine.connect() as conn:
    query = sqlalchemy.select(movies_table)
    results = conn.execute(query)
    for row in results:
        print(row)
        
#####################################
# sol using sqlalchemy
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///users.db', echo=True)

users_to_insert = [
    {'first_name': 'Sarah', 'last_name': 'Perry', 'email_address': 'sarah.perry@gmail.com'},
    {'first_name': 'Felix', 'last_name': 'Martin', 'email_address': 'felix_martin@gmail.com'}
    ]

with engine.connect() as conn:
    q = sqlalchemy.text(''' create table if not exists Users(user_id integer primary key autoincrement, first_name text, last_name text, email_address text)''')

    conn.execute(q)

    q = sqlalchemy.text('''insert into Users (first_name, last_name, email_address) VALUES (:first_name, :last_name,
                        :email_address)''')
    
    conn.execute(q, users_to_insert)

    q = sqlalchemy.text('''select * from Users''')

    result = conn.execute(q)
    for row in result:
        print(row)

    conn.commit()
    
#####################################
# using sqlalchemy expression language
metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("users", metadata,
                sqlalchemy.Column('user_id', sqlalchemy.Integer, primary_key=True),
                sqlalchemy.Column('first_name', sqlalchemy.String),
                sqlalchemy.Column('last_name', sqlalchemy.String),
                sqlalchemy.Column('email_address', sqlalchemy.String),
                
                )

metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users_to_insert))
    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)
    conn.commit()
#####################################
#####################################
#####################################