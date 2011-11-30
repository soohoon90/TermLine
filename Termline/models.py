from sqlalchemy import Table, Column, Integer, String, Text, \
                        DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from Termline.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    
    entries = relationship("Entry", backref='user')    

    def __init__(self, un=None, pw=None):
        self.username = un
        self.password = pw

    def __repr__(self):
        return '<User %r>' % (self.username)
        
class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    data = Column(Text)
    title = Column(Text)
    date = Column(DateTime)
    date2 = Column(DateTime)
    uid = Column(Integer, ForeignKey('user.id'))
    
    def __init__(self, data=None, uid=None):
        self.data = data
        self.uid = uid
    
    def __repr__(self):
        return '<Entry %r>' % (self.id)
