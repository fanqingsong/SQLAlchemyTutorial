# 3. Relationship

For full documentation visit [sqlalchemy.org](https://www.sqlalchemy.org/).

## Code

```python

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
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("parent_table.id"))
    parent = relationship("Parent", back_populates="children")


engine = create_engine("sqlite://", echo=True)

#engine = create_engine("sqlite:///./file.db", echo=True)

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
```


## Output

    2023-03-28 23:22:23,422 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-28 23:22:23,422 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("parent_table")
    2023-03-28 23:22:23,422 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-28 23:22:23,422 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("child_table")
    2023-03-28 23:22:23,422 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-28 23:22:23,422 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-28 23:22:23,424 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-28 23:22:23,424 INFO sqlalchemy.engine.Engine INSERT INTO parent_table (name) VALUES (?)
    2023-03-28 23:22:23,424 INFO sqlalchemy.engine.Engine [generated in 0.00011s] ('father',)
    2023-03-28 23:22:23,424 INFO sqlalchemy.engine.Engine INSERT INTO child_table (name, parent_id) VALUES (?, ?)
    2023-03-28 23:22:23,424 INFO sqlalchemy.engine.Engine [generated in 0.00010s] ('son', 8)
    2023-03-28 23:22:23,424 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-28 23:22:23,431 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-28 23:22:23,431 INFO sqlalchemy.engine.Engine SELECT parent_table.id AS parent_table_id, parent_table.name AS parent_table_name 
    FROM parent_table
    2023-03-28 23:22:23,431 INFO sqlalchemy.engine.Engine [generated in 0.00011s] ()
    '-------- p[0] ----------'
    <__main__.Parent object at 0x0000020F9489A3A0>
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000020F94854940>,
    'id': 1,
    'name': 'father'}
    '-------- p[0].children[0] ----------'
    2023-03-28 23:22:23,431 INFO sqlalchemy.engine.Engine SELECT child_table.id AS child_table_id, child_table.name AS child_table_name, child_table.parent_id AS child_table_parent_id 
    FROM child_table 
    WHERE ? = child_table.parent_id
    2023-03-28 23:22:23,431 INFO sqlalchemy.engine.Engine [generated in 0.00010s] (1,)
    <__main__.Child object at 0x0000020F948B3040>
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000020F9486AD60>,
    'id': 1,
    'name': 'son',
    'parent_id': 1}
    2023-03-28 23:22:23,431 INFO sqlalchemy.engine.Engine SELECT child_table.id AS child_table_id, child_table.name AS child_table_name, child_table.parent_id AS child_table_parent_id 
    FROM child_table
    2023-03-28 23:22:23,431 INFO sqlalchemy.engine.Engine [generated in 0.00008s] ()
    '-------- c[0] ----------'
    <__main__.Child object at 0x0000020F948B3040>
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000020F9486AD60>,
    'id': 1,
    'name': 'son',
    'parent_id': 1}
    '-------- c[0].parent ----------'
    <__main__.Parent object at 0x0000020F9489A3A0>
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000020F94854940>,
    'children': [<__main__.Child object at 0x0000020F948B3040>],
    'id': 1,
    'name': 'father'}
    '-------- c[0].parent.children[0] ----------'
    <__main__.Child object at 0x0000020F948B3040>
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000020F9486AD60>,
    'id': 1,
    'name': 'son',
    'parent': <__main__.Parent object at 0x0000020F9489A3A0>,
    'parent_id': 1}

