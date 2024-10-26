from flask import Blueprint, render_template, redirect, url_for
from app.models import Resource

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.mods'))

@main.route('/mods')
def mods():
    # 这里可以添加获取 MOD 列表的逻辑
    return render_template('mods.html')

@main.route('/modpacks')
def modpacks():
    # 这里可以添加获取整合包列表的逻辑
    return render_template('modpacks.html')

@main.route('/resourcepacks')
def resourcepacks():
    # 这里可以添加获取材质包列表的逻辑
    return render_template('resourcepacks.html')

@main.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)
