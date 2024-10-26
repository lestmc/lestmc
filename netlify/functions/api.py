from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from flask_serverless import FlaskServerless

app = create_app()
handler = FlaskServerless(app).handler
