from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost/laravel_github', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class ActivityUser(Base):
    __tablename__= 'activity_users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return '<ActivityUser {}>'.format(self.id)

    def save(self):
        db_session.add(self)
        db_session.commit()

class SocialUser(Base):
    __tablename__= 'social_users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    social_id = Column(String)
    social_type = Column(String)
    avatar = Column(String)
    nickname = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return '<SocialUser {}>'.format(self.id)

    def save(self):
        db_session.add(self)
        db_session.commit()
