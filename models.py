from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost/laravel_github', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class ActivityUser(Base):
    __tablename__= 'activities_user'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return '<ActivityUser {}>'.format(self.user_id)

    def save(self):
        db_session.add(self)
        db_session.commit()

