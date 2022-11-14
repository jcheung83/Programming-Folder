from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/')
def index():
    return "Welcome, go to /authors to begin"

@app.route('/authors')         
def authors():
    authors = Author.get_all()
    return render_template("index.html", authors=authors)

@app.route('/books')
def books():
    books = Book.get_all()
    return render_template("books.html", books=books)

@app.route('/create_author', methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    Author.save(data)
    return redirect('/authors')

@app.route('/create_book', methods=['POST'])
def create_book():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    Book.save(data)
    return redirect('/books')

@app.route('/authors/<id>')
def view_authors(id):
    data = {
        "id": id
    }
    fav_books = Book.get_favorites(data)
    info = Author.get_info_from_id(data)
    books = Book.get_all()
    return render_template("author.html", books=fav_books, info=info, all_books=books)

@app.route('/books/<id>')
def view_books(id):
    data = {
        "id": id
    }
    fav_authors = Author.get_favorites(data)
    info = Book.get_info_from_id(data)
    authors = Author.get_all()
    print(info)
    return render_template("book.html", authors=fav_authors, info=info, all_authors=authors)

@app.route('/favorite_a_book', methods=['POST'])
def favorite_a_book():
    data = {
        "author_id": request.form['author_id'],
        "book_id": request.form['book_id']
    }
    id = request.form['author_id']
    Author.favorite_book(data)
    return redirect(f'/authors/{id}')

@app.route('/favorite_b_book', methods=['POST'])
def favorite_b_book():
    data = {
        "author_id": request.form['author_id'],
        "book_id": request.form['book_id']
    }
    id = request.form['book_id']
    Author.favorite_book(data)
    return redirect(f'/books/{id}')