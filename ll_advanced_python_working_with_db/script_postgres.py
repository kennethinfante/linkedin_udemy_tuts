#####################################
# search for EDB postgres
# install except the pgAdmin4

# add to PATH the installation drive in C
# start postgres services
'''
$ psql -U postgres

postgres=# create database red30;
postgres=# \l
postgres=# \c red30;

$ pip install psycopg2-binary
'''

#####################################
# using psycopg2
import psycopg2 as pg

conn = pg.connect(database="red30",
                  user="postgres",
                  password="password",
                  host="localhost",
                  port="5432"
                  )

cursor = conn.cursor()

cursor.execute('''CREATE TABLE Sales(order_num int primary key,
cust_name text,
prod_number text,
prod_name text,
quantity int,
price real,
discount real,
order_total real
);''')

conn.commit()
conn.close()


#####################################
# insert
sales = [(1100935, "Spencer Educators", "DK204", "BYOD-300", 2, 89, 0, 178),
    (1100948, "Ewan Ladd", "TV810", "Understanding Automation", 1, 44.95, 0, 44.95),
    (1100963, "Stehr Group", "DS301", "DA-SA702 Drone", 3, 399, .1, 1077.3),
    (1100971, "Hettinger and Sons", "DS306", "DA-SA702 Drone", 12, 250, .5, 1500),
)
]

cursor.executemany("insert into sales values(%s, %s, %s, %s, %s, %s, %s, %s)", sales)
conn.commit()
conn.close()
#####################################
# insert interactively

def insert_sale(cur, order_num, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity

if __name__ == "__main__":
    conn = pg.connect(database="red30",
                  user="postgres",
                  password="password",
                  host="localhost",
                  port="5432"
                  )

    cur = conn.cursor()
    print("Input sale data:\n")
    order_num = int(input("What is the order number?\n"))
    cust_name = input("What is the customer name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("What is the product name?\n")
    quantity = float(input("What is the product name?\n"))
    price = float(input("What is the price of the product?\n"))
    discount = float(input("What is the discount, if there is one?\n"))
    print("Inputting sale data\n")
    insert_sale(cur, order_num, cust_name, prod_number, prod_name, quantity, price, discount)
    conn.commit()
    conn.close()

#####################################
# in this course, we use
# sqlite - sqlite3 module, sqlalchemy core
# mysql - mysql-connector, full sqlalchemy orm
# postgres - psycopg2 adapter, sqlalchemy core, full sqlalchemy orm

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, select

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/red30", echo=True)

metadata = MetaData()

# sales_table = Table("sales",
#                     metadata,
#                     Column('order_num', Integer, primary_key=True),
#                     Column('cust_name', String),
#                     Column('prod_number', String),
#                     Column('prod_name', String),
#                     Column('quantity', Float),
#                     Column('price', Float),
#                     Column('discount', Float),
#                     Column('order_total', Float)
#                     )

sales_table = Table('sales', metadata, autoload_with=engine)
metadata.create_all(engine)

with engine.connect() as conn:
    # read
    for row in conn.execute(select(sales_table)):
        print(row)

    # create
    insert_statement = sales_table.insert().values(order_num=1105910,
                                                   cust_name='Syman Mapstone',
                                                   prod_number = 'EB521',
                                                   prod_name = 'Understanding Artificial Intelligence',
                                                   quantity = 3,
                                                   price = 19.5,
                                                   discount = 0,
                                                   order_total = 58.5
                                                   )
    
    conn.execute(insert_statement)

    # update
    update_statement = sales_table.update().where(sales_table.c.order_num==1105910).value(quantity=2, order_total=29)
    conn.execute(update_statement)

    # confirm update
    reselect_stm = sales_table.select().where(sales_table.c.order_num==1105910)
    updated_sale = conn.execute(reselect_stm).first()
    print(updated_sale)

    # delete
    delete_stm = sales_table.delete().where(sales_table.c.order_num==1105910)
    conn.execute(delete_stm)

    # confirm delete
    not_found_stm = conn.execute(reselect_stm)
    print(not_found_stm.rowcount)
#####################################
# using sqlalchemy orm
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/red30", echo=True)

# class Sale(Base):
#     __tablename__ = 'sales'
#     Column('order_num', Integer, primary_key=True)
#     Column('cust_name', String)
#     Column('prod_number', String)
#     Column('prod_name', String)
#     Column('quantity', Float)
#     Column('price', Float)
#     Column('discount', Float)
#     Column('order_total', Float)

# or another method without writing the classes
Base = automap_base()

Base.prepare(autoload_with=engine)

Sales = Base.classes.sales

with Session(engine) as session:
    # read
    smallest_sale = session.execute(select(Sales).order_by(Sales.order_total)).scalar()
    print(smallest_sale.order_total)

    # insert
    recent_sale = Sales(order_num=1105910, cust_name='Syman Mapstone', cust_name='Syman Mapstone',
                                                   prod_number = 'EB521',
                                                   prod_name = 'Understanding Artificial Intelligence',
                                                   quantity = 3,
                                                   price = 19.5,
                                                   discount = 0,
                                                   order_total = 58.5)
    
    session.add(recent_sale)
    session.commit()

    # update
    recent_sale.quantity = 2
    recent_sale.order_total = 39
    updated_sale = session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()
    print(updated_sale.quantity)
    print(updated_sale.order_total)
    session.commit()

    # delete
    returned_sale = session.execute(select(Sales).filter(Sales.order_num == 1105910)).scalar()
    session.delete(returned_sale)
    session.commit()
#####################################
'''
postgres=# create database library;
postgres=# \l
postgres=# \c library;
'''

from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import registry, Session, relationship

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/library", echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    def __repr__(self):
        return "<Author(author_id='{0}', firstname='{1}', last_name='{2}')>" \
                .format(self.author_id, self.first_name, self.last_name)

class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    number_of_pages = Column(Integer)

    def __repr__(self):
        return "<Book(book_id='{0}', title='{1}', number_of_pages='{2}')>" \
                .format(self.book_id, self.title, self.number_of_pages)
    
class BookAuthor(Base):
    __tablename__  = 'bookauthors'
    bookauthor_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))

    author = relationship("Author")
    book = relationship("Book")

    def __repr__(self):
        return "<Book(bookauthor_id='{0}', author_id='{1}', book_id='{2}')>" \
                .format(self.bookauthor_id, self.author_id, self.book_id)
    
Base.metadata.create_all(engine)

def add_book(title, number_of_pages, first_name, last_name):
    author = Author(first_name=first_name, last_name=last_name)
    book = Book(title=title, number_of_pages=number_of_pages)

    with Session(engine) as session:
        existing_book = session.execute(select(Book).filter(Book.title==title, Book.number_of_pages==number_of_pages))
        if existing_book is not None:
            print("Book exists! Not adding book")
            return
        
    print("Book does not exist. Adding book")
    session.add(book)
    existing_author = session.execute(select(Author).filter(first_name==first_name, last_name==last_name))

    if existing_author is not None:
        print("Author exists! Not adding author")
        session.flush()
        pairing=BookAuthor(author_id=existing_author.author_id, book_id=book.book_id)
    else:
        print("Author does not exist. Adding author")
        session.add(author)
        session.flush()
        pairing = BookAuthor(author_id=author.author_id, book_id=book.book_id)

    session.add(pairing)
    session.commit()
    print("New pairing added!" + str(pairing))

if __name__ == "__main__":
    print("Input new book:\n")
    title = input("What is the title of the book?\n")
    number_of_pages = int(input("How many pages are in the book?\n"))
    first_name = input("What is the first name of the author?\n")
    last_name = input("what is the last name of the author?\n")
    print("Inputting book data:\n")

    add_book(title, number_of_pages, first_name, last_name)

    print("Done!")
#####################################