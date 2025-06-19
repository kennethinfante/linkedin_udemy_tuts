import schemas as sc
import database as db

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def get_root():
    return "Welcome to the books api"

@app.get("/book/{book_id}")
def retrieve_book(book_id: int):
    try:
        return db.get_book(book_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=repr(e))

@app.post("/book/")
def create_book(request: sc.BookAuthorPayload):
    book = _convert_into_book_db_model(request.book)
    author = _convert_into_author_db_model(request.author)

    db.add_book(book, author)
    return "New book added " + request.book.title + " " + str(request.book.number_of_pages) \
    + " New author added " + request.author.first_name + " " + request.author.last_name


def _convert_into_book_db_model(book: sc.Book):
    return db.Book(title=book.title, number_of_pages=book.number_of_pages)

def _convert_into_author_db_model(author: sc.Author):
    return db.Author(first_name=author.first_name, last_name=author.last_name)