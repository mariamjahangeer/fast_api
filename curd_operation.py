from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class book(BaseModel):
    id:int
    title:str
    author:str
    price:float
    available:bool
books=[]
# create(post)
@app.post("/books")
def add_books(book:Book):
    books.apend(book)
    return{"message":"book added","data":book}
# read(get)
@app.get("/books")
def read_books():
    return books

# read single book by id
@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book.id==book_id:
            return books
raise HTTPException(status_code=404,detail="book not found")


# update(put)

@app.put("/books/{book_id}")
def update_book(book_id:int,updated_book:Book):
    for index ,books in enumerstor(books):
        if book.id==book_id:
            books[index]=updated_book
            return{"message":"book_updated","data":updated_book}
        raise HTTPException(status_code=404,detail="book not found")
    
    # deletion

    @app.delete("/books/{book_id}")
    def delete_book(book_id:int):
        for book in books:
            if book.id==book_id:
                books.remove(book) 
                return{"message":f"book{book_id}deleted"}
raise HTTPException(status_code=404,detail="book not found")