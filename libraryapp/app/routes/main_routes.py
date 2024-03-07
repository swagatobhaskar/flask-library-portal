from flask import Blueprint, render_template

from app.extensions import db
from ..models import User, Subscription

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def hello():
    return "<p>Hello, world!</p>"

@main_bp.route('/users')
def get_all_users():
    users = User.query.all()
    return render_template('users.html', users=users)

# @app.route('/genres')
# def get_book_genres():
#     genres = Genre.query.all()
#     return render_template('book_genres.html', genres=genres)    

# @app.route('/authors')
# def get_all_authors():
#     authors = Author.query.all()
#     return render_template('authors.html', authors=authors)
