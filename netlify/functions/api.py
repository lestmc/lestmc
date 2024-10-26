from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from flask_serverless import FlaskServerless

app = create_app()

@app.route('/')
def index():
    return "Welcome to LestMC!"

@app.route('/test')
def test():
    return "Hello from Netlify!"

handler = FlaskServerless(app).handler
