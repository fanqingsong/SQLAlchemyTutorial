from pprint import pprint

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# using sqlite memory mode
engine = create_engine("sqlite://", echo=True)

# using sqlite file mode
#engine = create_engine("sqlite:///./file.db", echo=True)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

new_user = User(id='5', name='Bob')

session.add(new_user)

session.commit()

user = session.query(User).filter(User.id=='5').one()
print('type:', type(user))
print('name:', user.name)

session.delete(user)

session.commit()

users = session.query(User).filter(User.id=='5').all()
print('users:', users)

session.close()





