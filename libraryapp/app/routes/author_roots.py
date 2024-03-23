from flask import Blueprint, render_template

from app.extensions import db
# from ..models import User, Subscription

author_bp = Blueprint('author', __name__)#, template_folder='author_pages')

@author_bp.route("/all")
def all_authors():
    return render_template('author_pages/all_authors.html')
