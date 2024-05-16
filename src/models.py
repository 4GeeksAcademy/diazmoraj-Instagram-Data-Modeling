import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'

    followerid = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.userid'))
    user_from_id_relationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.userid'))
    user_to_id_relationship = relationship(User)

class Post(Base):
    __tablename__ = 'post'

    postid = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.userid'))
    user_id_relationship = relationship(User)

class Media(Base):
    __tablename__ = 'media'

    mediaid = Column(Integer, primary_key=True)
    type = Column(Enum, nullable=False)
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('post.postid'))
    post_id_relationship = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'

    commentid = Column(Integer, primary_key=True)
    comment_text = Column(String(max), nullable=False)
    author_id = Column(Integer, ForeignKey('user.userID'))
    author_id_relationship = relationship(User)
    post_id = Column(Integer, ForeignKey('post.postid'))
    post_id_relationship = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
