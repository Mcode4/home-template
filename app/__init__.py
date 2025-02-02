from flask import Flask, render_template
from .config import Configure
from .routes import content_route, about_us_route, contact_route

app = Flask(__name__)
app.config.from_object(Configure)
app.register_blueprint(content_route.bp)
app.register_blueprint(about_us_route.bp)
app.register_blueprint(contact_route.bp)

@app.route('/')
def home():
    return render_template('home_page.html')
