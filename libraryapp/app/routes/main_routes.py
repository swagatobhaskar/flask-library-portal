from flask import Blueprint, render_template

from app.extensions import db
from ..models import User, Subscription

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
@main_bp.route("/home")
def home():
    return render_template('home.html')

@main_bp.route('/users')
def get_all_users():
    users = User.query.all()
    return render_template('user_pages/users.html', users=users)

@main_bp.route('/contact')
def contact():
    return render_template('contact_us.html')
