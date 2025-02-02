from flask import Blueprint, render_template

bp = Blueprint('about_us', __name__, url_prefix='/about-us')

bp.route('/')
def main_page():
    return render_template('about_us.html')