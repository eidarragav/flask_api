from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(30), nullable= False, unique = True)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text, nullable = False)
    published = db.Column(db.Boolean, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {'id': self.id, 'titel': self.tile}
    





    
class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key = True, )
    name = db.Column(db.String(200), nullable =True)