# app.py
from flask import Flask, request, jsonify
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

# Function to create tables
with app.app_context():
    db.create_all()

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data.get('title'),
        author=data.get('author'),
        published_date=data.get('published_date'),
        isbn=data.get('isbn'),
        pages=data.get('pages'),
        cover=data.get('cover'),
        language=data.get('language')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get_or_404(book_id)

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.published_date = data.get('published_date', book.published_date)
    book.isbn = data.get('isbn', book.isbn)
    book.pages = data.get('pages', book.pages)
    book.cover = data.get('cover', book.cover)
    book.language = data.get('language', book.language)

    db.session.commit()
    return jsonify(book.to_dict()), 200

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
