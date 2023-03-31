# 6. Relationship with cascade

For full documentation visit [sqlalchemy.org](https://docs.sqlalchemy.org/en/14/orm/cascades.html#).


## Code

```py

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


```


## Output

    
    2023-03-31 23:29:18,959 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-31 23:29:18,959 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("parent_table")
    2023-03-31 23:29:18,959 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("parent_table")
    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("child_table")
    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("child_table")
    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine [raw sql] ()
    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine 
    CREATE TABLE parent_table (
        id INTEGER NOT NULL, 
        name VARCHAR, 
        PRIMARY KEY (id)
    )


    2023-03-31 23:29:18,960 INFO sqlalchemy.engine.Engine [no key 0.00005s] ()
    2023-03-31 23:29:18,967 INFO sqlalchemy.engine.Engine 
    CREATE TABLE child_table (
        id INTEGER NOT NULL, 
        name VARCHAR, 
        parent_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(parent_id) REFERENCES parent_table (id) ON DELETE CASCADE
    )


    2023-03-31 23:29:18,967 INFO sqlalchemy.engine.Engine [no key 0.00015s] ()
    2023-03-31 23:29:18,971 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-31 23:29:18,974 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-31 23:29:18,975 INFO sqlalchemy.engine.Engine INSERT INTO parent_table (name) VALUES (?)
    2023-03-31 23:29:18,975 INFO sqlalchemy.engine.Engine [generated in 0.00011s] ('father',)
    2023-03-31 23:29:18,976 INFO sqlalchemy.engine.Engine INSERT INTO child_table (name, parent_id) VALUES (?, ?)
    2023-03-31 23:29:18,976 INFO sqlalchemy.engine.Engine [generated in 0.00010s] ('son', 1)
    2023-03-31 23:29:18,977 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-31 23:29:18,980 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-31 23:29:18,981 INFO sqlalchemy.engine.Engine SELECT parent_table.id AS parent_table_id, parent_table.name AS parent_table_name 
    FROM parent_table
    2023-03-31 23:29:18,981 INFO sqlalchemy.engine.Engine [generated in 0.00009s] ()
    '-------- p ----------'
    [<__main__.Parent object at 0x0000018FC5702F70>]
    '-------- p[0] ----------'
    <__main__.Parent object at 0x0000018FC5702F70>
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000018FC5789640>,
    'id': 1,
    'name': 'father'}
    2023-03-31 23:29:18,983 INFO sqlalchemy.engine.Engine SELECT child_table.id AS child_table_id, child_table.name AS child_table_name, child_table.parent_id AS child_table_parent_id 
    FROM child_table 
    WHERE ? = child_table.parent_id
    2023-03-31 23:29:18,983 INFO sqlalchemy.engine.Engine [generated in 0.00013s] (1,)
    2023-03-31 23:29:18,984 INFO sqlalchemy.engine.Engine DELETE FROM child_table WHERE child_table.id = ?
    2023-03-31 23:29:18,984 INFO sqlalchemy.engine.Engine [generated in 0.00014s] (1,)
    2023-03-31 23:29:18,986 INFO sqlalchemy.engine.Engine DELETE FROM parent_table WHERE parent_table.id = ?
    2023-03-31 23:29:18,986 INFO sqlalchemy.engine.Engine [generated in 0.00011s] (1,)
    2023-03-31 23:29:18,986 INFO sqlalchemy.engine.Engine COMMIT
    2023-03-31 23:29:18,989 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2023-03-31 23:29:18,989 INFO sqlalchemy.engine.Engine SELECT parent_table.id AS parent_table_id, parent_table.name AS parent_table_name 
    FROM parent_table
    2023-03-31 23:29:18,989 INFO sqlalchemy.engine.Engine [cached since 0.008214s ago] ()
    '-------- p ----------'
    []
    2023-03-31 23:29:18,990 INFO sqlalchemy.engine.Engine SELECT child_table.id AS child_table_id, child_table.name AS child_table_name, child_table.parent_id AS child_table_parent_id 
    FROM child_table
    2023-03-31 23:29:18,990 INFO sqlalchemy.engine.Engine [generated in 0.00009s] ()
    '-------- c ----------'
    []

    Process finished with exit code 0
