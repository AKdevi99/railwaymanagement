from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/book-ticket')
@login_required
def book_ticket():
    return render_template("book_ticket.html", user=current_user)

@views.route('/schedule')
@login_required
def schedule():
    return render_template("schedule.html", user=current_user)