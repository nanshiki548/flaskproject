from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from apps import models, forms

# Create the instance of SQLAlchemy
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    # Initialize SQLAlchemy and LoginManager with this Flask app, if not initialized yet
    db.init_app(app)
    login_manager.init_app(app)

    Migrate(app, db)

    login_manager.login_view = 'index'
    login_manager.login_message = ''

    @app.route('/', methods=['GET','POST'])
    def index():
        form = forms.SignupForm()
        if form.validate_on_submit():
            user = models.User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
            )
            if user.is_duplicate_email():
                flash("登録済みのメールアドレスです")
                return redirect(url_for('index'))
            
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    
        return render_template('index.html', form=form)
    
    from apps.authapp.views import authapp
    app.register_blueprint(authapp, url_prefix='/auth')

    from apps.pictapp.views import pictapp
    app.register_blueprint(pictapp, url_prefix='/picture')

    return app
