from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy
DB_Name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HVVGBVGKI JUBGUOBGO'
    app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_Name}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app