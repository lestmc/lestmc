from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='.')  # 更改模板文件夹为根目录
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app
