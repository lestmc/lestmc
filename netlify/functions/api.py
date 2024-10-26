from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from flask_serverless import FlaskServerless
import os

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css', mimetype='text/css')

@app.route('/mods')
def mods():
    return render_template('mods.html')

@app.route('/modpacks')
def modpacks():
    return render_template('modpacks.html')

@app.route('/resourcepacks')
def resourcepacks():
    return render_template('resourcepacks.html')

@app.route('/resources')
def resources():
    # 这里你可能需要从数据库获取资源
    resources = []  # 替换为实际的资源列表
    return render_template('resources.html', resources=resources)

handler = FlaskServerless(app).handler
