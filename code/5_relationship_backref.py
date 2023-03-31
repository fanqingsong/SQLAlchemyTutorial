from pprint import pprint

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Parent(Base):
    __tablename__ = "parent_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parent_table.id"))
    parent = relationship("Parent", backref="children")


engine = create_engine("sqlite:///./file.db", echo=True)
Base.metadata.create_all(engine)

session = sessionmaker(engine)()


p = Parent()
p.name = "father"

c1 = Child()
c1.name = "son"
p.children = [c1]

session.add_all([p, c1])
session.commit()


p = session.query(Parent).all()

pprint("-------- p[0] ----------")

pprint(p[0])
pprint(p[0].__dict__)


pprint("-------- p[0].children[0] ----------")

pprint(p[0].children[0])

pprint(p[0].children[0].__dict__)


c = session.query(Child).all()

pprint("-------- c[0] ----------")

pprint(c[0])

pprint(c[0].__dict__)

pprint("-------- c[0].parent ----------")

pprint(c[0].parent)

pprint(c[0].parent.__dict__)


pprint("-------- c[0].parent.children[0] ----------")

pprint(c[0].parent.children[0])

pprint(c[0].parent.children[0].__dict__)






