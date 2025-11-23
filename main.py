from fastapi import FastAPI, HTTPException
# yochay abergel ID 211657531
app = FastAPI()

# "מסד נתונים בזכרון
books = [
    {"id": "1", "title": "FirstBook", "author" : "lidor"},
    {"id": "2", "title": "SecBook", "author" : "Hads"},
    {"id": "3", "title": "ThirdBook", "author" : "Yochay"},
    {"id": "4", "title": "LastBook", "author" : "Itay"}
]
counter = 1

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id : int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
def add_book(book: dict):
    global counter
    new_book = {
        "id" : counter,
        "title" : book.get("title"),
        "author": book.get("author")
    }
    books.append(new_book)
    counter += 1
    return new_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message":"Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")