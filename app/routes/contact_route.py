from flask import Blueprint, render_template

bp = Blueprint('contact', __name__, url_prefix='/contact')

bp.route('/')
def main_page():
    return render_template('contact.html')