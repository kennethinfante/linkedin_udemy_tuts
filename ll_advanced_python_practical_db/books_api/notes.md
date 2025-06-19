# DB  Setup
note in mac, there are two passwords to enter
first the computer password, then the mysql root password

in windows, add the C:\Program Files\MySQL\MySQL Server 8.0\bin to path

```
$ create database books;

# then the database.py

$ use books;
$ show tables;
$ describe bookauthor;
```

# Add book

Run server
`$ uvicorn main:app --reload`

Send to `127.0.0.1:8000/book/`
In the Body, add raw -> JSON

```
{
    "book" : {
        "title" : "The Huntress",
        "number_of_pages": 560
    },
    "author" : {
        "first_name": "Kate",
        "last_name": "Quinn"
    }
}
```

# Add Book to db
```
{
    "book" : {
        "title" : "Where the Crawdads Sing",
        "number_of_pages": 386
    },
    "author" : {
        "first_name": "Delia",
        "last_name": "Owens"
    }
}
```