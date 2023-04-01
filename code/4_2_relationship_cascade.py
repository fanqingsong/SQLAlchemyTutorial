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
    children = relationship(
        "Child",
        back_populates="parent",
        cascade="all, delete, save-update"
    )


class Child(Base):
    __tablename__ = "child_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parent_table.id", ondelete="CASCADE"))
    parent = relationship("Parent", back_populates="children")


engine = create_engine("sqlite:///.file.db", echo=True)
Base.metadata.create_all(engine)

session = sessionmaker(engine)()


p = Parent()
p.name = "father"

c1 = Child()
c1.name = "son"
p.children = [c1]

session.add_all([p])
session.commit()


p = session.query(Parent).all()

pprint("-------- p ----------")

pprint(p)

pprint("-------- p[0] ----------")

pprint(p[0])
pprint(p[0].__dict__)

# session.delete(p[0].children[0])

session.delete(p[0])

session.commit()

p = session.query(Parent).all()

pprint("-------- p ----------")

pprint(p)

c = session.query(Child).all()

pprint("-------- c ----------")

pprint(c)


