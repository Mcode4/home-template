from flask import Blueprint, render_template

bp = Blueprint('content', __name__, url_prefix='/content')

bp.route('/')
def main_page():
    return render_template('content.html')