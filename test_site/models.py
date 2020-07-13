from test_site import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Profile.query.get(int(user_id))

class Profile(db.Model, UserMixin) :       
    ___tablename__="profile"
    id=db.Column(db.Integer, primary_key=True)  #define each row in the table
    name_=db.Column(db.String(30))               #, unique=True)
    language_=db.Column(db.String(30))
    age_=db.Column(db.String(30))
    posts = db.relationship('Response',backref='author', lazy=True)

    def __init__ (self, name_,language_,age_):  #initialising instance variables
        self.name_=name_
        self.language_=language_
        self.age_=age_

#one-to-many relationship
class Response(db.Model) :       
    ___tablename__="response"
    id=db.Column(db.Integer, primary_key=True)  #define each row in the table
    question_=db.Column(db.String(10))
    answer_user_=db.Column(db.Integer)
    answer_correct_=db.Column(db.Integer)
    time_=db.Column(db.Integer)
    answer_status_=db.Column(db.Integer)
    user_id= db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)

    def __init__ (self, question_, answer_user_,answer_correct_,answer_status_ ,time_,user_id):  #initialising instance variables
        self.question_=question_
        self.answer_user_=answer_user_
        self.answer_correct_=answer_correct_
        self.answer_status_=answer_status_
        self.time_=time_
        self.user_id=user_id
