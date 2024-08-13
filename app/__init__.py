# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app,db)

# from app import routes, models




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Create instances of the extensions
db = SQLAlchemy()
ckeditor = CKEditor()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 's1cr1tk1'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the extensions with the app
    db.init_app(app)
    ckeditor.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        # Import routes to register them with the app
        from . import routes
        routes.init_app(app)

        from app.models import Post
        # Create database tables
        db.create_all()
        # Setup Flask-Admin
        admin = Admin(app, name='Admin', template_mode='bootstrap3')
        admin.add_view(ModelView(Post, db.session))

    return app