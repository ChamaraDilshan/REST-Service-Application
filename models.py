# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    published_date = db.Column(db.String(10), nullable=True)
    isbn = db.Column(db.String(13), nullable=True)
    pages = db.Column(db.Integer, nullable=True)
    cover = db.Column(db.String(250), nullable=True)
    language = db.Column(db.String(2), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "published_date": self.published_date,
            "isbn": self.isbn,
            "pages": self.pages,
            "cover": self.cover,
            "language": self.language
        }
