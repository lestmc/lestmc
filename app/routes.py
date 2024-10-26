from flask import Blueprint, render_template
from app.models import Resource

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)
