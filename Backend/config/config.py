from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:zaryab@localhost/drawing'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "hellowrodl"
    db.init_app(app)
