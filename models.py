from exts import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model,):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(20),nullable=False)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(100),nullable=False)

    def __init__(self,*args,**kwargs):
        email=kwargs.get('email')
        username=kwargs.get('username')
        password=kwargs.get('password')

        self.email=email
        self.username=username
        self.password=generate_password_hash(password)

    def check_password(self,raw_password):
        result=check_password_hash(self.password,raw_password)
        return result

class Question(db.Model):
    __tablename__='question'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship("User", backref=db.backref('questions'))
    content_ps=db.Column(db.Text)


class Answer(db.Model):
    __tablename__='answer'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,)
    content=db.Column(db.Text,nullable=False)
    question_id=db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question = db.relationship("Question", backref=db.backref('answers',order_by=id.desc()))
    author = db.relationship("User", backref=db.backref('aquestions'))
