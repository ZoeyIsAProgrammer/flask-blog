from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.DevelopmentConfig")
    Bootstrap(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.get_or_404(User, user_id)

    from .auth import auth
    from .main import main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app

# with app.app_context():
#     db.create_all()

# with app.app_context():
#     blog = Blog(title="Blog Post 2", body="Blog Post 1 Content")
#     db.session.add(blog)
#     db.session.commit()