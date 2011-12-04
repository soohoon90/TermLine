from Termline import db

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    
    entries = db.relationship("Image", backref='user')    

    def __init__(self, un=None, pw=None):
        self.username = un
        self.password = pw

    def __repr__(self):
        return '<User %r>' % (self.username)
        
class Image(db.Model):
    __tablename__ = 'image'
    iid = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Text)
    data = db.Column(db.Text)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    
    def __init__(self, data=None, uid=None):
        self.data = data
        self.uid = uid
    
    def __repr__(self):
        return '<Image %r>' % (self.iid)
